import torch
from torch import nn
from torchvision.utils import make_grid
import matplotlib.pyplot as plt

torch.manual_seed(0)


def plot_images_from_tensor(
    image_tensor,
    num_images=25,
    size=(1, 28, 28),
    title=None
):
    # Normalize the image tensor to [0, 1]
    image_tensor = (image_tensor + 1) / 2

    # Detach + move to CPU
    img_detached = image_tensor.detach().cpu()

    # Create a grid of images
    image_grid = make_grid(img_detached[:num_images], nrow=5)

    plt.imshow(image_grid.permute(1, 2, 0).squeeze())
    if title is not None:
        plt.title(title)
    plt.show()



def make_grad_hook():

    # List to store the gradients
    gradients_list = []

    def grad_hook(m):
        if isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):
            gradients_list.append(m.weight.grad)

    return gradients_list, grad_hook


'''
Model weights initialization with normal distribution, and optionally add bias depending on m
'''
def weights_init(m):
    if isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):
        torch.nn.init.normal_(m.weight, 0.0, 0.02)
    if isinstance(m, nn.BatchNorm2d):
        torch.nn.init.normal_(m.weight, 0.0, 0.02)
        torch.nn.init.constant_(m.bias, 0)


'''
Generate latent noise vector
'''
def get_noise(n_samples, z_dim, device="cpu"):
    return torch.randn(n_samples, z_dim, device=device)


"""
Calculate generator loss by maximizing D(G(z))
I.e., it tries to maximize the discriminator's output for fake instances
"""


def get_gen_loss(critic_fake_prediction):
    gen_loss = -1.0 * torch.mean(critic_fake_prediction)
    return gen_loss


# Test generator loss calculation
assert torch.isclose(get_gen_loss(torch.tensor(1.0)), torch.tensor(-1.0))

assert torch.isclose(get_gen_loss(torch.rand(10000)), torch.tensor(-0.5), 0.05)

print("Success!")

'''
Calculate critic loss by maximizing D(x) - D(G(z))
'''
def get_crit_loss(critic_fake_prediction, crit_real_pred, gp, c_lambda):
    crit_loss = (
        torch.mean(critic_fake_prediction) - torch.mean(crit_real_pred) + c_lambda * gp
    )
    return crit_loss


# Test critic loss calculation
assert torch.isclose(
    get_crit_loss(torch.tensor(1.0), torch.tensor(2.0), torch.tensor(3.0), 0.1),
    torch.tensor(-0.7),
)
assert torch.isclose(
    get_crit_loss(torch.tensor(20.0), torch.tensor(-20.0), torch.tensor(2.0), 10),
    torch.tensor(60.0),
)

print("Success!")