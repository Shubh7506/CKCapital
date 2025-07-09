import os
import datetime

def save_screenshot_on_fail(item, call):
    print(f"save_screenshot_on_fail called for {item.name}, phase: {call.when}")
    if call.when == 'call':
        outcome = call.excinfo
        if outcome is not None:
            driver = getattr(item, 'driver', None)
            if driver is not None:
                screenshots_dir = os.path.join(os.getcwd(), 'screenshots')
                if not os.path.exists(screenshots_dir):
                    os.makedirs(screenshots_dir)
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = f"{item.name}_{timestamp}.png"
                filepath = os.path.join(screenshots_dir, filename)
                try:
                    driver.save_screenshot(filepath)
                    print(f"Screenshot saved to {filepath}")
                except Exception as e:
                    print(f"Failed to take screenshot: {e}")