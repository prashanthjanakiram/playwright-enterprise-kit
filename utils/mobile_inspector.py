"""Mobile vs Desktop element inspector for responsive testing."""

class MobileInspector:
    def __init__(self, page):
        self.page = page
    
    def compare_elements(self, url, elements):
        """
        Compare element visibility across viewports.
        
        Args:
            url: Page to test
            elements: List of selectors e.g. ['#login-btn', '.hamburger-menu']
        """
        results = []
        
        # Desktop viewport
        self.page.set_viewport_size({"width": 1920, "height": 1080})
        self.page.goto(url)
        
        for selector in elements:
            visible = self.page.locator(selector).is_visible(timeout=5000)
            results.append({
                "selector": selector,
                "desktop_visible": visible,
                "recommendation": "✅ Good" if visible else "⚠️ Check mobile"
            })
        
        # Mobile viewport
        self.page.set_viewport_size({"width": 375, "height": 667})
        self.page.reload()
        
        for result in results:
            mobile_visible = self.page.locator(result["selector"]).is_visible(timeout=3000)
            result["mobile_visible"] = mobile_visible
            if not mobile_visible and result["desktop_visible"]:
                result["recommendation"] = "🔥 MOBILE ISSUE: Hidden on mobile"
        
        return results