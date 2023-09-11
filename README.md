<h1 align="center">Valorant Lineup Tool</h1>
<p align="center">
<img src="https://github.com/Simonrye/testing_repo/assets/85827801/db482cf5-4132-4f61-8d3f-cb452793622a" width="50%" height="50%"/>
</p>

<div>
This tool is designed to assist players in creating on-the-spot lineups for specific agents. Stand nearly anywhere within range, and you'll receive an overlay to guide the lineup. The tool analyzes the minimap to determine the exact distance and direction of the spike, then places a convenient overlay on your Valorant game screen. With this tool, anyone can quickly and easily create precise lineups from anywhere on the map. Importantly, this script does not interact with the game files, ensuring it remains entirely external. For a better understanding of how the script works, expand the videos below.
<br />
This project was created for the purpose of quickly setting up memorable lineups in custom games for later use.
</div>
<h3 align="center" width="100%">Agents</h3>
<h5>Brimstone: Incendiary</h5>
<details>
<summary><b>Brimstone Video Demos</b></summary>


https://github.com/Simonrye/valorant-lineup-tool/assets/85827801/9ecd9daa-3f87-45ee-9955-d2d85240361a


https://github.com/Simonrye/valorant-lineup-tool/assets/85827801/c73c23aa-9fe3-4a6d-93ea-c22e8610841f
</details>
When you're far enough, you'll see two indicators: an 'X' for a bounce landing and a dot for a direct hit.
<br />
Direct hits may be needed when a backboard is present and the terrain in front of the spike prevents a predictable bounce. 
<br />

*Some computers may have trouble rendering the second indicator, which may distrupt the script.*
<h5>Viper: Snake Bite</h5>
<details>
<summary><b>Viper Video Demo</b></summary>


https://github.com/Simonrye/valorant-lineup-tool/assets/85827801/21f364b9-a7ca-4731-921b-dee09b4fcabd
</details>
The extreme range of a Snake Bite, paired with the direct impact when landing makes Viper the best agent for this tool. 
<br />
The trajectory is less affected by elevation differences.
<h5>KAY/O: FRAG/ment</h5>
<details>
<summary><b>KAY/O Video Demo</b></summary>


https://github.com/Simonrye/valorant-lineup-tool/assets/85827801/b660febe-5c62-4af2-8754-83a3f9a531a6
</details>
This projectile is limited by it's shorter reach, but still works close range.
<br />
This projectile is underdeveloped, and still may present issues.
<h3 align="center">Setup</h3>

1. **Dependencies:** Be sure to have installed the nessessary Python libraries.
   * `pip install Pillow`
   * `pip install pynput`
   * `pip install PyAutoGUI`

3. **Configure Your Settings:** *Compatible settings are crucial for the script to function!*
   * Disable mouse acceleration if it's enabled. (It's often enabled by default on Windows)
   * Open `settings.json` and adjust the valorant sensitivity value to match your own.
   * Launch Valorant and ensure the mini-map settings are set as:
     * Rotate: `Rotate`
     * Keep Player Centered: `On`
     * Minimap Size: `1`
     * Minimap Zoom: `1`

<h3 align="center">Usage</h3>

1. **Running the Script:**
   * Download the entire "Valorant-Lineup-Tool" folder found in this repo. Inside lies the Python script.
   * If you are trying the script for the first time, choosing Viper, Breeze, and an unplanted spike is recommended.
   * Start a custom Valorant game with cheats enabled and run the Python file.
   * Select the same agent and map of choice for both Valorant and the script.
   * Select whether you want to aim at a planted or unplanted spike in the script.

2. **Create lineup:** 
   * Drop or plant the bomb (depending on selected choice earlier) at a point of your choosing.
   * Move to your location of choice for the lineup.
   * Somewhat face the direction of the spike. *As long as the spike is not "behind" you on the minimap it's okay.*
   * Look straight down, and let go of your mouse.
   * Hit the right arrow key. *It is good practice to hit the left arrow once before this to prevent any past lineup confliction.*
   * Slowly look up and find the X that marks the spot to shoot the projectile. Do not open the map, or any other UI such as Brimstone's smokes or ultimate (E- Sky Smokes, X- Orbital Strike) during this time until projectile is fired.
   * Once fired, hit the left arrow to reset the X. Repeat.

<h3 align="center">Troubleshooting</h3>

1. **Change spike RGB values:** Issues may arise if you had applied any color enhancements to your computer.
   * Start a custom game with cheats enabled.
   * Drop the spike and take a screenshot of it on the minimap.
   * Open the screenshot with a tool such as Paint 3D to extract the required RGB from the spike.
   * Ensure that you select a pixel color that accurately represents the majority of the spike.
   * Open `settings.json` and edit the respective value.
   * Repeat this process for a planted spike.

2. **Adjust Map Multiplier** If you find that the projectile consistently falls short or goes too far, follow these steps:
   * Enter a custom game, preferly on the Icebox map.
   * Launch the script while selecting the same map.
   * Choose a corner that allows for maximum distance, positioning yourself as far away as possible while maintaining a clear view of the spike.
   * Ping the spike to get the distance (in meters). Then press the right arrow, then the left arrow.
   * Compare the in-game distance with the distance displayed in the console.
   * Make the necessary adjustments in the `settings.json` file; you'll find more detailed instructions there.

<h3 align="center">How Does It Work?</h3>

<details>
<summary>Watch the Explanation Video</summary>


https://github.com/Simonrye/valorant-lineup-tool/assets/85827801/6042b287-4205-487a-8283-f4470051d60c
</details>

The script operates by utilizing the centered minimap and the spike's RGB information to determine the player's fixed position and the relative position of the spike. This data is used to calculate the distance and direction to the spike. Subsequently, the script places an "X" overlay onto the screen, intended to guide the player precisely where to aim in-game. To initiate the lineup, the player must look straight down to align the "X" with the correct y-position.

When you switch away from the Valorant window while keeping the minimap in view, the script will continue to function as expected. See the video above.

As Valorant directly uses raw input from the mouse itself, the script attempts to accurately track the in-game mouse movements through the cursor's position. However, there may be slight discrepancies between raw mouse movement and cursor position, which is why extreme mouse movement will cause desync. Additionally, mouse cursors are confined within the monitor boundaries, while raw mouse movement is not. This explains why the mouse DPI is intentionally reduced to prevent any cursor collisions with the top of the screen when aiming upward in-game during a lineup.

The calculations for converting distance (in meters) to a y-offset were determined through a trial-and-error process, resulting in reasonably accurate functions. This method is far from flawless.

Each map in Valorant has a distinct pixel-to-distance (in meters) ratio, which is why map-specific multipliers were included in the `settings.json` file. These multipliers are rough estimations and are not precise.

<h3 align="center">IMPORTANT NOTICE</h3>
<p>
Please read this section carefully before using this tool.
</p>
<p>
 
**Disclaimer:** The tool is **NOT** affiliated with Valorant. Exercise caution when using it in custom games. I have not and will not test this script during live games as a precaution. The script **DOES NOT** interact with any game files. Any responsibility for using this script will solely rest upon the user who chooses to use it.
</p>
<p>
 
**The most intrusive actions taken by this script include:**

* Reading your screen to locate the bomb
* Displaying a small overlay (X) above all your windows
* Tracking the mouse cursor position to move the overlay accordingly
* Placing the mouse cursor at the bottom of your screen at the start of ever lineup
* Changing mouse DPI during the lineup
</p>
<p>
 
**Important:** This tool temperarily changes your DPI during a lineup. If you notice your mouse moving unusually slowly outside of Valorant, click the left arrow to reset the DPI. If the script is closed, you can run the script again to reset the DPI. To prevent this, always remember to click the left arrow after completing a lineup, and avoid closing the script in the middle of a lineup.
</p>
