# ComfyUI-ResolutionSelector

A simple and editable **resolution preset selector** node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

This custom node lets you quickly select common image or video resolutions from a dropdown list, or define your own manual resolution.  
Presets are stored in a separate `resolutions.json` file that you can freely edit — no code change or restart required.

---

## Features

- ✅ Dropdown list of predefined image/video resolutions  
- ✅ Easy manual input via “Custom (manual input)” option  
- ✅ External `resolutions.json` file — editable at runtime  
- ✅ Works with **Reload Custom Nodes** (no restart)  
- ✅ Clean output: `(width, height)` for direct wiring to `Empty Latent Image`, `WANVideo`, etc.

---

## 📁 Folder structure

ComfyUI/custom_nodes/  
└── ResolutionSelector/  
├── init.py  
├── ResolutionSelector.py  
└── resolutions.json  

---

## Installation

1. Go to your ComfyUI `custom_nodes` folder.
2. Clone this repository:
   ```bash
   git clone https://github.com/dodemedexter/ComfyUI-ResolutionSelector.git

## Usage

Find it under the Utilities category:
Utilities → Resolution Selector
Select a preset (e.g. WAN - 9:16 HD [544x960 portrait])
Connect the outputs:
(width, height) → Empty Latent Image

## 🧾 Editing the presets

The list of resolutions is stored in resolutions.json.
You can edit this file freely to add, rename, or remove entries.

Example:
{  
    "IMAGE 1:1 [1024x1024 square]": {"width": 1024, "height": 1024},  
    "WAN - 9:16 HD [544x960 portrait]": {"width": 544, "height": 960},  
    "Custom (manual input)": {"width": 512, "height": 512}  
}  

After editing, just click Reload Custom Nodes in ComfyUI Manager — no need to restart.

## Dependencies

None.
This node uses only the standard ComfyUI API and the Python standard library.

## License

This project is released under the MIT License
