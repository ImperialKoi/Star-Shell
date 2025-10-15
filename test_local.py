#!/usr/bin/env python3
"""
Quick test script for star-shell package
"""

def test_imports():
    """Test that all modules can be imported"""
    try:
        import star_shell
        from star_shell.main import app
        from star_shell.backend import OpenAIGenie, GeminiGenie
        from star_shell.utils import get_os_info
        print("✅ All imports successful!")
        print(f"📦 Package version: {star_shell.__version__}")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_cli_help():
    """Test that CLI help works"""
    import subprocess
    try:
        result = subprocess.run(['star-shell', '--help'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ CLI help command works!")
            return True
        else:
            print(f"❌ CLI help failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ CLI test error: {e}")
        return False

def test_os_info():
    """Test utility functions"""
    try:
        from star_shell.utils import get_os_info
        os_family, os_fullname = get_os_info()
        print(f"✅ OS detection works: {os_family} - {os_fullname}")
        return True
    except Exception as e:
        print(f"❌ OS info test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing star-shell package locally...")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_cli_help, 
        test_os_info
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Tests passed: {passed}/{len(tests)}")
    
    if passed == len(tests):
        print("🎉 All tests passed! Package is ready for PyPI!")
    else:
        print("⚠️  Some tests failed. Check the issues above.")