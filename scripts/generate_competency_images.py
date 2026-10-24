#!/usr/bin/env python3
"""Batch generate slide 19 competency scenes via Google Flow Brave CDP."""

import os
import sys
import time

sys.path.append("/mnt/data/projects/insta-bonus-miner/submodules/toon-studio/scripts")
from flow_image import FlowImageClient, log

SCENES = [
    (
        "slides/02-essence/assets/competency_02_harness.png",
        "An automated software quality assurance test harness loop in a high-tech futuristic laboratory. Code packets moving through a circular conveyor tunnel with holographic laser scanners and bright green checkmark checkpoint gates. Passing code glow emerald green and proceed, while flagged code is redirected by a robotic feedback rail back to an AI terminal. Isometric 3D, sleek cybernetic UI, emerald green and charcoal palette, hyper-detailed."
    ),
    (
        "slides/02-essence/assets/competency_03_specification.png",
        "An AI coding agent entity navigated along a high-precision laser guidance rail system built from glowing floating documentation tablets and modular skill blocks labeled Skills, Rules, Context Specs. Golden and violet guide tracks keeping the AI on a tight, flawless trajectory without drifting. Minimalist sci-fi, crisp glowing typography, dark purple and amber gold ambient lighting, 3D concept art."
    ),
    (
        "slides/02-essence/assets/competency_04_security.png",
        "A multi-layered hexagonal translucent energy shield protecting a glowing database core and server cluster from external crimson glitch spikes and malicious data penetration attempts. A human security architect operates a holographic defense control console, tuning security policies while the energy shield repels incoming threats. Futuristic cybersecurity command center, crimson threats vs luminous cobalt blue shield, 8k octane render."
    ),
]

def main():
    cdp_url = os.environ.get("FLOW_CDP_URL", "http://127.0.0.1:9222")
    debug_dir = "static/flow-debug"
    
    client = FlowImageClient(cdp_url, debug_dir)
    if not client.connect():
        log("❌ Failed to connect over CDP.")
        return 1

    try:
        for out_path, prompt in SCENES:
            if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
                log(f"⏭️ Skipping already generated: {out_path}")
                continue
            
            log(f"\n🎨 Starting generation for: {out_path}")
            log(f"   Prompt: {prompt[:80]}...")
            
            ok = client.generate_one(prompt, out_path, timeout=180, aspect="16:9")
            if not ok or not os.path.exists(out_path):
                log(f"❌ Failed to generate: {out_path}")
                return 1
            
            log(f"✅ Finished: {out_path} ({os.path.getsize(out_path)} bytes)")
            time.sleep(3)
        
        log("\n🎉 All competency scenes generated successfully!")
        return 0
    finally:
        client.close()

if __name__ == "__main__":
    sys.exit(main())
