import sys
import re


def modify_html_file(file_path):
    try:
        # Open the file for reading
        with open(file_path, "r", encoding="utf-8") as file:
            file_contents = file.read()

        # Change the loading screen
        file_contents = re.sub(re.escape(r'''<style id="style-init-screen" type="text/css">@-webkit-keyframes init-loading-spin{0%{-webkit-transform:rotate(0);transform:rotate(0)}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}@-o-keyframes init-loading-spin{0%{-o-transform:rotate(0);transform:rotate(0)}100%{-o-transform:rotate(360deg);transform:rotate(360deg)}}@keyframes init-loading-spin{0%{-webkit-transform:rotate(0);-o-transform:rotate(0);transform:rotate(0)}100%{-webkit-transform:rotate(360deg);-o-transform:rotate(360deg);transform:rotate(360deg)}}#init-screen{display:none;z-index:500000;position:fixed;top:0;left:0;height:100%;width:100%;font:28px/1 Helmet,Freesans,sans-serif;font-weight:700;color:#eee;background-color:#111;text-align:center}#init-screen>div{display:none;position:relative;margin:0 auto;max-width:1136px;top:25%}html[data-init=lacking] #init-screen,html[data-init=loading] #init-screen,html[data-init=no-js] #init-screen{display:block}html[data-init=lacking] #init-lacking,html[data-init=no-js] #init-no-js{display:block;padding:0 1em}html[data-init=no-js] #init-no-js{color:red}html[data-init=loading] #init-loading{display:block;border:24px solid transparent;border-radius:50%;border-top-color:#7f7f7f;border-bottom-color:#7f7f7f;width:100px;height:100px;-webkit-animation:init-loading-spin 2s linear infinite;-o-animation:init-loading-spin 2s linear infinite;animation:init-loading-spin 2s linear infinite}html[data-init=loading] #init-loading>div{text-indent:9999em;overflow:hidden;white-space:nowrap}html[data-init=loading] #passages,html[data-init=loading] #ui-bar{display:none}</style>'''), '''<style id="style-init-screen" type="text/css">
  #init-screen {
      display: none;
      z-index: 500000;
      position: fixed;
      top: 0;
      left: 0;
      height: 100%;
      width: 100%;
      font: 28px/1 var(--body-font);
      font-weight: 700;
      color: #eee;
      background-color: var(--background);
      background-image: var(--background-image);
      text-align: center;
  }
  
  #init-screen > div {
      display: none;
      position: relative;
      margin: 0 auto;
      max-width: 1136px;
      top: 50%;
      transform: translateY(-50%);
  }
  html[data-init="lacking"] #init-screen,
  html[data-init="loading"] #init-screen,
  html[data-init="no-js"] #init-screen {
      display: block;
  }
  html[data-init="lacking"] #init-lacking,
  html[data-init="no-js"] #init-no-js {
      display: block;
      padding: 0 1em;
  }
  html[data-init="no-js"] #init-no-js {
      color: red;
  }
  html[data-init="loading"] #init-loading {
      display: block;
  }
  html[data-init="loading"] #passages,
  html[data-init="loading"] #ui-bar {
      display: none;
  }

  .text-shimmer {
    margin: 0 auto;
    padding: 0;
    display: inline;
    margin-bottom: 0;
    background-repeat: no-repeat;
    background-size: 200% 100%;
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 8s infinite;
    background-color: white;
    background-image: linear-gradient(to right, white, var(--blue), white);
    transform: translateZ(0);
  }

  @keyframes shimmer {
      0% {
          background-position: 100% 0;
      }
      100% {
          background-position: 0 0;
      }
  }
</style>''', file_contents)
        
        file_contents = re.sub(r'''	<div id="init-screen">
		<div id="init-no-js"><noscript>JavaScript must be enabled to play.</noscript></div>
		<div id="init-lacking"><p>Browser lacks capabilities required to play.</p><p>Upgrade or switch to another browser.</p></div>
		<div id="init-loading"><div>Loading&hellip;</div></div>
	</div>''', '''  <div id="init-screen">
    <div id="init-no-js"><noscript>JavaScript must be enabled to play.</noscript></div>
    <div id="init-lacking"><p>Browser lacks capabilities required to play.</p><p>Upgrade or switch to another browser.</p></div>
    <div id="init-loading"><span class="text-shimmer">Loading...</span></div>
  </div>''', file_contents)

        # Prevent flash of unstyled content (edit: does not work)
        #         file_contents = file_contents.replace(
        #             f"""<meta charset="UTF-8" />""",
        #             f"""<meta charset="UTF-8" />
        # <style>html{{visibility: hidden;opacity:0;\}}</style>""",
        #         )

        # Add more meta tags
        file_contents = file_contents.replace(
            f"""<meta name="viewport" content="width=device-width,initial-scale=1" />""",
            f"""<meta name="viewport" content="width=device-width,initial-scale=1" />
<meta name="description" content="An interactive fiction game about fighting your former friend." />
<meta property="og:title" content="You Can&#39;t Save Her" />
<meta property="og:description" content="An interactive fiction game about fighting your former friend." />
<meta property="twitter:description" content="An interactive fiction game about fighting your former friend." />

<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
<link rel="manifest" href="site.webmanifest">
<meta name="msapplication-TileColor" content="#2b5797">
<meta name="theme-color" content="#ffffff">""",
        )

        # Write the modified contents back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_contents)

        print(f"{file_path} has been modified successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_html_file>")
    else:
        file_path = sys.argv[1]
        modify_html_file(file_path)
