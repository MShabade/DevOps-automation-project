from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <html>
    <head>
        <title>Deployment Demo</title>
        <style>
            body { font-family: Arial, sans-serif; text-align:center; padding:50px; background:#f7f7f7; }
            h1 { color:#333; }
            .card { display:inline-block; width:250px; margin:20px; padding:20px; 
                    background:white; border-radius:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1); }
            .manual { border-top: 4px solid #f39c12; }
            .automation { border-top: 4px solid #27ae60; }
        </style>
    </head>
    <body>
        <h1>Deployment Demo</h1>
        <div class="card manual">
            <h2>Manual</h2>
            <p>Deployed by hand on EC2.</p>
        </div>
        <div class="card automation">
            <h2>Automation</h2>
            <p>Terraform + Ansible + GitHub Actions</p>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
