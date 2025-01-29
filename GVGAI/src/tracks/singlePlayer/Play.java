package tracks.singlePlayer;

import tracks.ArcadeMachine;



public class Play {
    public static void main(String[] args) {
        String game = "examples\\gridphysics\\zelda.txt";
        boolean visuals = true;
        String agentName = "tracks.singlePlayer.tools.human.Agent";
        String actionFile = null;
        int randomSeed = 0; 
        int playerID = 0;

        for (int i = 0; i < 1024; i++) { 
            String level = "C:\\InternshipProject\\Levels\\level_data\\generatedLevels\\processed_levels\\constructiveLevelGenerator\\zelda_lvl" + i + ".txt";
            String screenshotFile = "C:\\InternshipProject\\Levels\\level_data\\final_levels\\constructive_img\\zelda_lvl" + i + ".jpg";
            // String level = "C:\\InternshipProject\\Levels\\level_data\\processed_levels\\randomLevelGenerator\\zelda_lvl" + i + ".txt";
            // String screenshotFile = "C:\\InternshipProject\\Levels\\level_data\\final_levels\\random_img\\zelda_lvl" + i + ".jpg";
            // String level = "C:\\InternshipProject\\Levels\\level_data\\processed_levels\\customLevels\\zelda_lvl" + i + ".txt";
            // String screenshotFile = "C:\\InternshipProject\\Levels\\level_data\\final_levels\\custom_img\\zelda_lvl" + i + ".jpg";

            //Call getScreenShot for each level file and screenshot destination
            ArcadeMachine.getScreenShot(game, level, visuals, agentName, actionFile, randomSeed, playerID, screenshotFile);
        }
    }
}