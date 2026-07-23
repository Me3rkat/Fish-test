from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clic', methods=['POST'])
def capture_clic():
    user_ip = request.remote_addr
    # On récupère le nom envoyé en JSON
    donnees = request.get_json()
    nom_utilisateur = donnees.get('nom', 'Anonyme')
    
    # Notification ultra-claire dans ton terminal
    print(f"\n📢 [ALERTE TIRAGE]")
    print(f"👤 NOM : {nom_utilisateur}")
    print(f"🌐 IP  : {user_ip}")
    print(f"---------------------------\n")
    
    # Sauvegarde dans le fichier
    with open("participations.txt", "a", encoding="utf-8") as f:
        f.write(f"Nom: {nom_utilisateur} | IP: {user_ip}\n")
        
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)