import os
import json
import torch
import comfy.model_management as mm

class ResolutionSelector:
    _resolutions = {}
    _json_error = None

    @classmethod
    def _load_presets(cls):
        json_path = os.path.join(os.path.dirname(__file__), "resolutions.json")
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            valid = {}
            for name, wh in data.items():
                if name.strip().lower() == "custom (manual input)".lower():
                    continue
                if isinstance(wh, dict) and "width" in wh and "height" in wh:
                    w, h = int(wh["width"]), int(wh["height"])
                    if w > 0 and h > 0:
                        valid[name] = {"width": w, "height": h}
            cls._resolutions = valid
            cls._json_error = None
        except Exception as e:
            cls._resolutions = {}
            cls._json_error = str(e)

    @classmethod
    def INPUT_TYPES(cls):
        cls._load_presets()
        preset_names = list(cls._resolutions.keys())
        preset_names.append("Custom (manual input)")
        if cls._json_error:
            preset_names.insert(0, f"Error loading resolutions.json: {cls._json_error}")

        return {
            "required": {
                "preset": (preset_names,),
                "custom_width":  ("INT", {"default": 1024, "min": 64, "max": 8192, "step": 8}),
                "custom_height": ("INT", {"default": 1024, "min": 64, "max": 8192, "step": 8}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "LATENT")
    RETURN_NAMES = ("width", "height", "latent")
    FUNCTION = "run"
    CATEGORY = "Utilities/IO"

    def run(self, preset, custom_width, custom_height):
        cw, ch = int(custom_width), int(custom_height)

        # Sélection de la résolution
        if preset.startswith("Error loading") or preset == "Custom (manual input)":
            w, h = cw, ch
        elif preset in self._resolutions:
            res = self._resolutions[preset]
            w, h = int(res["width"]), int(res["height"])
        else:
            w, h = cw, ch

        # Génération d'une latente standard (1, 4, h/8, w/8)
        device = mm.get_torch_device()
        latent_tensor = torch.zeros((1, 4, max(1, h // 8), max(1, w // 8)), device=device)
        latent = {"samples": latent_tensor}

        return w, h, latent


NODE_CLASS_MAPPINGS = {
    "ResolutionSelector": ResolutionSelector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionSelector": "Resolution Selector"
}
