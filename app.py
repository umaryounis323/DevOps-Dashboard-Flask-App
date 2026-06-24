from flask import Flask
import psutil
import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    uptime_seconds = datetime.datetime.now().timestamp() - psutil.boot_time()
    uptime_hours = round(uptime_seconds / 3600, 2)

    return f'''
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Dashboard</title>
    <meta http-equiv="refresh" content="5">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: Arial, sans-serif;
            background: #0d1117;
            color: white;
            padding: 30px;
        }}
        h1 {{
            text-align: center;
            color: #58a6ff;
            margin-bottom: 10px;
            font-size: 36px;
        }}
        .subtitle {{
            text-align: center;
            color: #8b949e;
            margin-bottom: 40px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            max-width: 900px;
            margin: 0 auto;
        }}
        .card {{
            background: #161b22;
            border-radius: 12px;
            padding: 25px;
            border: 1px solid #30363d;
        }}
        .card h2 {{
            color: #58a6ff;
            margin-bottom: 15px;
            font-size: 18px;
        }}
        .stat {{
            font-size: 48px;
            font-weight: bold;
            color: #3fb950;
            margin-bottom: 5px;
        }}
        .stat.warning {{ color: #d29922; }}
        .stat.danger {{ color: #f85149; }}
        .label {{
            color: #8b949e;
            font-size: 14px;
        }}
        .progress-bar {{
            background: #30363d;
            border-radius: 10px;
            height: 10px;
            margin-top: 15px;
        }}
        .progress {{
            height: 10px;
            border-radius: 10px;
            background: #3fb950;
        }}
        .progress.warning {{ background: #d29922; }}
        .progress.danger {{ background: #f85149; }}
        .badge {{
            display: inline-block;
            background: #1f6feb;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            margin: 4px;
        }}
        footer {{
            text-align: center;
            margin-top: 40px;
            color: #8b949e;
            font-size: 13px;
        }}
    </style>
</head>
<body>
    <h1>🖥️ DevOps Dashboard</h1>
    <p class="subtitle">Built by Umar Younis | Auto-refreshes every 5 seconds</p>

    <div class="grid">
        <div class="card">
            <h2>⚡ CPU Usage</h2>
            <div class="stat {'danger' if cpu > 80 else 'warning' if cpu > 50 else ''}">{cpu}%</div>
            <div class="label">Current CPU Load</div>
            <div class="progress-bar">
                <div class="progress {'danger' if cpu > 80 else 'warning' if cpu > 50 else ''}" 
                     style="width: {cpu}%"></div>
            </div>
        </div>

        <div class="card">
            <h2>🧠 RAM Usage</h2>
            <div class="stat {'danger' if ram.percent > 80 else 'warning' if ram.percent > 50 else ''}">{ram.percent}%</div>
            <div class="label">{round(ram.used/1024/1024/1024, 2)} GB used of {round(ram.total/1024/1024/1024, 2)} GB</div>
            <div class="progress-bar">
                <div class="progress {'danger' if ram.percent > 80 else 'warning' if ram.percent > 50 else ''}"
                     style="width: {ram.percent}%"></div>
            </div>
        </div>

        <div class="card">
            <h2>💾 Disk Usage</h2>
            <div class="stat {'danger' if disk.percent > 80 else 'warning' if disk.percent > 50 else ''}">{disk.percent}%</div>
            <div class="label">{round(disk.used/1024/1024/1024, 2)} GB used of {round(disk.total/1024/1024/1024, 2)} GB</div>
            <div class="progress-bar">
                <div class="progress {'danger' if disk.percent > 80 else 'warning' if disk.percent > 50 else ''}"
                     style="width: {disk.percent}%"></div>
            </div>
        </div>

        <div class="card">
            <h2>⏱️ Server Uptime</h2>
            <div class="stat">{uptime_hours}h</div>
            <div class="label">Hours since last reboot</div>
        </div>
    </div>

    <div style="text-align:center; margin-top: 30px;">
        <span class="badge">🐳 Dockerized</span>
        <span class="badge">⚙️ CI/CD Pipeline</span>
        <span class="badge">🚂 Railway</span>
        <span class="badge">🐍 Flask</span>
        <span class="badge">📊 psutil</span>
    </div>

    <footer>
        <p>🚀 Deployed via GitHub Actions CI/CD | Umar Younis — DevOps Engineer</p>
    </footer>
</body>
</html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
