from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" type="text/css" href="https://sudor2spr.github.io/Documentation/assets/style.css">
    <titleSudoR2spr Repository</title>
	<link rel="icon" type="image/x-icon" href="">

</head>

<body>
    <div class="container" style="bg-dark text-red text-center py-3 mt-5">
        <a href="https://t.me/nklbotbackup" class="card">
            <p>
               ░█▀▀▄░▒█▄░▒█░▒█▀▀█░▒█▀▀▀░▒█░░░<br>
               ▒█▄▄█░▒█▒█▒█░▒█░▄▄░▒█▀▀▀░▒█░░░<br>
               ▒█░▒█░▒█░░▀█░▒█▄▄▀░▒█▄▄▄░▒█▄▄█<br>
                                             <br>

                <b>v2.0.0</b>
            </p>
        </a>
    </div>
	<br></br><br></br><br></br>
	<footer class="bg-dark text-white text-center py-3 mt-5">
	<center><img loading="lazy" class="object-none object-center" src="" width="60" height="60">
        Powered By CHIRU 
		<img loading="lazy" class="object-none object-center" src="" width="60" height="60">
		<div class="footer__copyright">
            <p class="footer__copyright-info">
                © 2024 Video Downloader. All rights reserved.
            </p>
        </div>
    </footer></center>
</body>

</html>
"""


if __name__ == "__main__":
    app.run()
