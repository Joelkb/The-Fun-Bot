echo "Cloning main Repository"
git clone https://github.com/Dev-f-k/The-Fun-Bot.git /The-Fun-Bot
cd /The-Fun-Bot
pip3 install -U -r requirements.txt
echo "Starting The-Fun-Bot..."
python3 bot.py
