from playwright.sync_api import sync_playwright
B="https://betrnames.github.io/water-treatment-guide/"
with sync_playwright() as p:
    br=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    for name,vp,mob in [("desktop",{"width":1280,"height":900},False),("mobile",{"width":390,"height":844},True)]:
        ctx=br.new_context(viewport=vp,is_mobile=mob,device_scale_factor=2 if mob else 1)
        pg=ctx.new_page(); errs=[]; pg.on("pageerror",lambda e: errs.append(str(e)))
        pg.goto(B,wait_until="networkidle"); pg.screenshot(path=f"screenshots/home-{name}.png",full_page=False)
        pg.goto(B+"softener-size-calculator/",wait_until="networkidle")
        pg.fill("#hard","15"); pg.fill("#iron","1"); pg.fill("#people","4"); pg.fill("#gpd","75"); pg.fill("#days","7")
        pg.click("button[type=submit]")
        out=pg.inner_text("#out"); print(name, "| calc:", out.replace("\n"," | "))
        assert "39,900" in out and "64,000" in out, "calc mismatch"
        pg.select_option("#unit","mgl"); pg.fill("#hard","171"); pg.fill("#iron","0"); pg.fill("#people","4")
        out2=pg.inner_text("#out"); print(name,"| mg/L test:", out2.split("\n")[0], "|", "10.0 gpg" in out2)
        pg.select_option("#unit","gpg"); pg.fill("#hard","15"); pg.fill("#iron","1")
        pg.locator("form.calc").scroll_into_view_if_needed()
        pg.locator("#out").scroll_into_view_if_needed()
        pg.screenshot(path=f"screenshots/calculator-{name}.png",full_page=False)
        print(name,"js errors:",errs)
        ctx.close()
    br.close()
