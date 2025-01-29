import torch
from torch import nn

torch.manual_seed(0)

'''
Generator
'''
class Generator(nn.Module):
    def __init__(self, z_dim=512, im_chan=3, hidden_dim=64):
        super().__init__()
        self.z_dim = z_dim
        self.generator = nn.Sequential(
            # 1) 1×1 -> 4×4
            self._build_gen_block(z_dim, hidden_dim*16, 4, 1, 0),
            # 2) 4×4 -> 8×8
            self._build_gen_block(hidden_dim*16, hidden_dim*8, 4, 2, 1),
            # 3) 8×8 -> 16×16
            self._build_gen_block(hidden_dim*8, hidden_dim*4, 4, 2, 1),
            # 4) 16×16 -> 32×32
            self._build_gen_block(hidden_dim*4, hidden_dim*2, 4, 2, 1),
            # 5) 32×32 -> 64×64
            self._build_gen_block(hidden_dim*2, hidden_dim, 4, 2, 1),
            # 6) 64×64 -> 128×128
            self._build_gen_block(hidden_dim, hidden_dim//2, 4, 2, 1),
            # 7) 128×128 -> 256×256
            nn.ConvTranspose2d(hidden_dim//2, im_chan, kernel_size=4, stride=2, padding=1),
            nn.Tanh()
        )

    def _build_gen_block(self, in_c, out_c, k, s, p):
        return nn.Sequential(
            nn.ConvTranspose2d(in_c, out_c, k, s, p, bias=False),
            nn.BatchNorm2d(out_c),
            nn.ReLU(inplace=True),
        )

    def forward(self, noise):
        x = noise.view(len(noise), self.z_dim, 1, 1)
        return self.generator(x)


'''
Critic
'''
class Critic(nn.Module):
    def __init__(self, im_chan=3, hidden_dim=64):
        super().__init__()
        self.critic = nn.Sequential(
            self._crit_block(im_chan, hidden_dim,    kernel_size=4, stride=2, padding=1),
            self._crit_block(hidden_dim, hidden_dim*2, kernel_size=4, stride=2, padding=1),
            self._crit_block(hidden_dim*2, hidden_dim*4, kernel_size=4, stride=2, padding=1),
            self._crit_block(hidden_dim*4, hidden_dim*8, kernel_size=4, stride=2, padding=1),
            self._crit_block(hidden_dim*8, hidden_dim*16, kernel_size=4, stride=2, padding=1),  
            self._crit_block(hidden_dim*16, 1, kernel_size=4, stride=1, padding=0, final_layer=True),
        )

    def _crit_block(self, in_channels, out_channels, kernel_size, stride, padding, final_layer=False):
        if not final_layer:
            return nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding, bias=False),
                nn.BatchNorm2d(out_channels),
                nn.LeakyReLU(0.2, inplace=True),
            )
        else:
            return nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding, bias=False),
                # Output shape: N×1×1×1, flatten in forward()
            )

    def forward(self, image):
        out = self.critic(image)
        return out.view(len(out), -1)  # Flatten to [N, 1]
    