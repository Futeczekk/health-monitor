from flask import Flask, jsonify
import socket
import platform
import time
import psutil


app = Flask(__name__)

START_TIME = time.time()


def get_system_stats():
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "hostname": socket.gethostname(),
        "system": platform.system(),
        "kernel": platform.release(),
        "uptime_seconds": int(time.time() - START_TIME),
        "ram_used_percent": ram.percent,
        "disk_used_percent": disk.percent
    }


@app.route("/")
def home():
    stats = get_system_stats()

    html = f"""
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>VPS Health Monitor</title>
        <style>
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: #111827;
                color: #f9fafb;
            }}

            .container {{
                max-width: 900px;
                margin: 60px auto;
                padding: 20px;
            }}

            .card {{
                background: #1f2937;
                border-radius: 18px;
                padding: 30px;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            }}

            h1 {{
                margin-top: 0;
                font-size: 36px;
            }}

            .status {{
                color: #22c55e;
                font-weight: bold;
            }}

            .grid {{
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 16px;
                margin-top: 24px;
            }}

            .box {{
                background: #374151;
                border-radius: 12px;
                padding: 18px;
            }}

            .label {{
                color: #9ca3af;
                font-size: 14px;
            }}

            .value {{
                margin-top: 8px;
                font-size: 22px;
                font-weight: bold;
            }}

            code {{
                background: #111827;
                padding: 4px 8px;
                border-radius: 8px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <h1>VPS Health Monitor</h1>

                <p>Status aplikacji: <span class="status">OK</span></p>
                <p>Endpoint techniczny: <code>/health</code></p>

                <div class="grid">
                    <div class="box">
                        <div class="label">Hostname</div>
                        <div class="value">{stats["hostname"]}</div>
                    </div>

                    <div class="box">
                        <div class="label">System</div>
                        <div class="value">{stats["system"]}</div>
                    </div>

                    <div class="box">
                        <div class="label">Kernel</div>
                        <div class="value">{stats["kernel"]}</div>
                    </div>

                    <div class="box">
                        <div class="label">Uptime aplikacji</div>
                        <div class="value">{stats["uptime_seconds"]} s</div>
                    </div>

                    <div class="box">
                        <div class="label">RAM użyty</div>
                        <div class="value">{stats["ram_used_percent"]}%</div>
                    </div>

                    <div class="box">
                        <div class="label">Dysk użyty</div>
                        <div class="value">{stats["disk_used_percent"]}%</div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    return html


@app.route("/health")
def health():
    stats = get_system_stats()

    return jsonify({
        "status": "ok",
        "service": "vps-health-monitor",
        "hostname": stats["hostname"],
        "uptime_seconds": stats["uptime_seconds"],
        "ram_used_percent": stats["ram_used_percent"],
        "disk_used_percent": stats["disk_used_percent"]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
