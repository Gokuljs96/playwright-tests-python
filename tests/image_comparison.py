from playwright.sync_api import sync_playwright
from PIL import Image, ImageChops


def compare_images(img1_path, img2_path):
    """
    Compare two images and display the differences.
    """
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # Ensure the images are the same size
    if img1.size != img2.size:
        print(f"Images are of different sizes: {img1.size} vs {img2.size}")
        return

    # Calculate the difference between the images
    diff = ImageChops.difference(img1, img2)

    if diff.getbbox():
        diff.show()  # Show the difference image
        print("Images are different.")
    else:
        print("Images are the same.")


# Main script to take screenshots and compare them
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Run in headless mode for faster execution
    page = browser.new_page()

    # Navigate to the page you want to capture
    page.goto("https://example.com")  # Replace with your target URL

    # Take the first screenshot
    page.screenshot(path='screenshot1.png')
    print("Screenshot 1 taken.")

    # Navigate to another page or make changes on the same page
    # For example, you can interact with the page here
    # page.click('selector')  # Uncomment and replace with an actual selector

    # Take the second screenshot
    page.screenshot(path='screenshot2.png')
    print("Screenshot 2 taken.")

    # Compare the two screenshots
    compare_images('screenshot1.png', 'screenshot2.png')

    # Close the browser
    browser.close()
