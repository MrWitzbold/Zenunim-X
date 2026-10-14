# Math Tools 🧮💥
### The laws of physics are more like suggestions, apparently.

A tiny Roblox math-and-utility GUI for people who look at a 3D map and think: *"This would be easier if I could put little red balls everywhere."*

**Math Tools** combines distance measuring, world annotations, freehand drawing, and a couple of movement toggles in one gloriously blue-and-yellow panel. It is not a sophisticated scientific instrument. It is, however, a collection of buttons that can make geometry a little less annoying.

> Made by **JUKjacker** · found in the MrWitzbold corner of the internet

---

## 🧰 What does it do?

| Feature | How it works |
|---|---|
| 📏 **Distance measuring** | Hold **Left Ctrl** and click a point in the world to place a numbered vertex. The script draws a beam between the latest pair and displays their distance. |
| 🏷️ **World labels** | Enter some text in the label box, then click **Add labels** and **Left Alt + click** a point to place it in the world. |
| ✏️ **Freehand drawing** | Use **Draw tool** to draw in 3D space. Your artistic masterpiece may look like geometry, modern art, or a network cable having a crisis. |
| 🧹 **Clear vertices** | Removes the measurement points and resets the vertex counter. |
| 🧽 **Clear drawings** | Removes drawing parts created under your character. |
| 📝 **Notes** | A built-in text box for whatever important calculations, coordinates, or deeply concerning observations you need to write down. |
| 🚶 **Toggle speed** | Switches your character's WalkSpeed between **16** and **100**. |
| 👻 **Noclip toggle** | The GUI offers an **F to noclip** button. See the caveat below: the current implementation has some key-handling inconsistencies. |
| 🫥 **Hide / Show** | Hide the main panel and bring it back with the floating button. |
| 🖱️ **Draggable GUI** | Move the main panel around the screen instead of letting it squat in the middle forever. |

## 🎮 Controls

- **Left Ctrl + click** — place a measurement vertex.
- **Left Alt + click** — place a text label at the targeted point (after activating the label button).
- **Toggle speed** — switch between WalkSpeed `16` and `100`.
- **F to noclip** — intended to toggle noclip; the current script's status text says `E` while the handler listens for `F`, so this feature deserves a cleanup pass.
- **Clear vertices** — delete measurement markers and reset measurement state.
- **Clear drawings** — delete the drawing parts currently parented to your character.
- **Hide / Show** — tuck away or restore the main panel.

## 🚀 Installation / execution

This file is a **Roblox client-side LocalScript-style GUI script**. It uses `Players.LocalPlayer`, `PlayerGui`, mouse input, the local character, and client-side workspace objects.

1. Open the script and review it before running it.
2. Use it only in an environment and Roblox experience where you have permission to run custom client-side scripts.
3. Run it in a compatible client-side context that supports the APIs it uses.
4. If you're adapting it for Roblox Studio, restructure it as a proper `LocalScript` and test it in a private place first.

This is not a normal Studio plugin or a standalone Lua program; pasting it into an arbitrary server Script will not make it work.

## ⚠️ Known quirks (the bugs are part of the archaeological record)

A few things worth knowing before you summon the blue rectangle:

- **Noclip needs fixing.** Clicking the button creates a key listener, but the UI says `F` while the debug message says `E`. The implementation also sets up its toggle inside the button callback, so repeated clicks can create additional listeners.
- **Drawing cleanup is local-character-specific.** The clear function only removes parts named `location` that are children of your current character.
- **Notes are not saved.** They live in the textbox; don't close the session expecting a diary entry to survive.
- **Labels and measurement markers are workspace objects.** The cleanup button is specifically for measurement vertices; it doesn't remove labels.
- **The drawing tool uses legacy Roblox APIs.** `HopperBin`, older event connections, and some deprecated removal patterns may need updating in modern Roblox environments.
- **This script assumes a character and Humanoid are available** for movement features. Respawning or running before character initialization may cause errors.
- **Distance is measured between the last two recorded vertices.** It reports Roblox world-space studs, not meters, centimeters, or legally binding surveying data.

## 🧪 Technical notes

- **Language:** Lua / Roblox Luau-style scripting
- **Interface:** `ScreenGui`, `Frame`, `TextButton`, `TextBox`, and `TextLabel`
- **Input:** mouse clicks and `UserInputService`
- **World visualization:** anchored Parts, `BillboardGui`, `Attachment`, and `Beam`
- **Movement:** `Humanoid.WalkSpeed` and Humanoid state changes

The script is written in an older, hand-assembled style, with each GUI button setting up its own behavior. It can serve as a starting point for experimentation, but it would benefit from refactoring: shared input handlers, safer character checks, modern event connections, and cleaner cleanup logic.

## 🧠 Why?

Because sometimes you need to measure a distance in a 3D world, leave yourself a label, draw a suspicious squiggle, and then move at WalkSpeed 100. The scientific method has had stranger afternoons.

## 📜 Disclaimer

This project is provided for educational and experimental use. Only run client-side scripts where you have permission, and follow the rules of the Roblox experience you're playing. Movement modifications and noclip-style behavior may violate individual game rules.

No warranty. No guarantees. The red balls are not certified by any professional surveying authority.

---

*Built with Roblox parts, questionable restraint, and a frankly unnecessary amount of blue.*

