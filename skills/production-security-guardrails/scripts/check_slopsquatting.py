#!/usr/bin/env python3
"""
Slopsquatting & Phantom Dependency Inspector
Verifies if a requested Python (PyPI) or JavaScript (npm) package is legitimate
or a newly registered / hallucinated squatting trap.
"""

import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone

def check_pypi(package_name: str):
    url = f"https://pypi.org/pypi/{package_name}/json"
    req = urllib.request.Request(url, headers={"User-Agent": "SecurityGuardrail/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            info = data.get("info", {})
            releases = data.get("releases", {})
            
            # Find earliest upload
            earliest_date = None
            for ver, files in releases.items():
                for f in files:
                    upload_time_str = f.get("upload_time_iso_8601")
                    if upload_time_str:
                        dt = datetime.fromisoformat(upload_time_str.replace("Z", "+00:00"))
                        if earliest_date is None or dt < earliest_date:
                            earliest_date = dt

            summary = info.get("summary", "No description")
            home_page = info.get("home_page") or info.get("project_url")
            version = info.get("version", "unknown")

            age_days = (datetime.now(timezone.utc) - earliest_date).days if earliest_date else 9999
            
            print(f"📦 PyPI Package: {package_name} (v{version})")
            print(f"   Summary: {summary[:80]}")
            print(f"   Home: {home_page}")
            if earliest_date:
                print(f"   Created: {earliest_date.strftime('%Y-%m-%d')} ({age_days} days ago)")
            
            if age_days < 30:
                print(f"⚠️  [ALERT] Package was registered recently ({age_days} days ago). Potential Slopsquatting risk!")
                return False
            else:
                print(f"✅ [SAFE] Package is established ({age_days} days old).")
                return True

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"🚨 [CRITICAL] Package '{package_name}' DOES NOT EXIST on PyPI!")
            print("   This is likely an AI HALLUCINATION. Do NOT register or install blindly.")
        else:
            print(f"⚠️ HTTP error checking PyPI: {e}")
        return False
    except Exception as e:
        print(f"⚠️ Failed to query PyPI: {e}")
        return False

def check_npm(package_name: str):
    url = f"https://registry.npmjs.org/{package_name}"
    req = urllib.request.Request(url, headers={"User-Agent": "SecurityGuardrail/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            time_data = data.get("time", {})
            created_str = time_data.get("created")
            
            created_dt = datetime.fromisoformat(created_str.replace("Z", "+00:00")) if created_str else None
            age_days = (datetime.now(timezone.utc) - created_dt).days if created_dt else 9999
            
            desc = data.get("description", "No description")
            latest = data.get("dist-tags", {}).get("latest", "unknown")
            
            print(f"📦 npm Package: {package_name} (v{latest})")
            print(f"   Description: {desc[:80]}")
            if created_dt:
                print(f"   Created: {created_dt.strftime('%Y-%m-%d')} ({age_days} days ago)")
                
            if age_days < 30:
                print(f"⚠️  [ALERT] Package is very young ({age_days} days old). Potential Slopsquatting risk!")
                return False
            else:
                print(f"✅ [SAFE] Package is established ({age_days} days old).")
                return True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"🚨 [CRITICAL] Package '{package_name}' DOES NOT EXIST on npm registry!")
            print("   This is an AI HALLUCINATION. Attackers may squat this name.")
        else:
            print(f"⚠️ HTTP error checking npm: {e}")
        return False
    except Exception as e:
        print(f"⚠️ Failed to query npm: {e}")
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: check_slopsquatting.py [pypi|npm] <package_name>")
        sys.exit(1)
        
    ecosystem = sys.argv[1].lower()
    pkg = sys.argv[2]
    
    if ecosystem in ("python", "pypi", "pip"):
        safe = check_pypi(pkg)
    elif ecosystem in ("node", "npm", "js"):
        safe = check_npm(pkg)
    else:
        print(f"Unknown ecosystem '{ecosystem}'. Use 'pypi' or 'npm'.")
        sys.exit(1)
        
    sys.exit(0 if safe else 1)

if __name__ == "__main__":
    main()
