echo "Cloning main Repository"
git clone https://github.com/Joelkb/Beta-dq-the-file-donor-.git /The-Fun-Bot
cd /The-Fun-Bot
pip3 install -U -r requirements.txt
echo "Starting DQ-The-File-Donor...."
python3 main.py
