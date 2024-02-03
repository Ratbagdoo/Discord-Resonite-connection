import subprocess

if __name__ == "__main__":
    subprocess.Popen(["python", "websoket_server_discord.py"])
    subprocess.Popen(["python", "discord_bot.py"])
    subprocess.Popen(["python", "Websocket_Server_Send"])
    # Add subprocess.Popen for new flies if needed
