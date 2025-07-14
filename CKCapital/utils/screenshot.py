import os
import datetime
import pytest
import pytest_html
from pytest_html import extras

def attach_screenshot_to_report(item, rep):
    driver = getattr(item, "funcargs", {}).get("driver", None)
    if driver:
        import tempfile, os
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
            screenshot_path = tmpfile.name
            driver.save_screenshot(screenshot_path)
            with open(screenshot_path, "rb") as f:
                image_data = f.read()
            if hasattr(rep, "extra"):
                rep.extra.append(extras.image(image_data, mime_type="image/png"))
            else:
                rep.extra = [extras.image(image_data, mime_type="image/png")]
        os.remove(screenshot_path)