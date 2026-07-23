from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clic', methods=['POST'])
def capture_clic():
    # 1. Capture de l'IP
    # Si tu es derrière un proxy (ex: Heroku), utilise request.headers.get('X-Forwarded-For', request.remote_addr)
    user_ip = request.remote_addr
    
    # 2. Capture du type d'appareil (User-Agent)
    user_agent = request.headers.get('User-Agent')
    
    # Analyse simplifiée de l'appareil
    device = "Ordinateur"
    if "Mobile" in user_agent or "Android" in user_agent or "iPhone" in user_agent:
        device = "Mobile / Tablette"

    # 3. Capture du nom envoyé par le formulaire
    donnees = request.get_json()
    nom_utilisateur = donnees.get('nom', 'Anonyme')
    
    # 4. Horodatage
    heure = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # AFFICHAGE DANS LA CONSOLE (Notification visuelle)
    print(f"\n🔥 [NOUVELLE ACTIVITÉ - {heure}]")
    print(f"👤 NOM      : {nom_utilisateur}")
    print(f"🌐 IP       : {user_ip}")
    print(f"📱 APPAREIL : {device}")
    print(f"📄 AGENT    : {user_agent[:50]}...") # Coupe pour la lisibilité
    print(f"--------------------------------------------\n")
    
    # 5. SAUVEGARDE DANS UN FICHIER LOG
    with open("journal_tirage.txt", "a", encoding="utf-8") as f:
        f.write(f"[{heure}] Nom: {nom_utilisateur} | IP: {user_ip} | Appareil: {device}\n")
        
    return jsonify(success=True)

if __name__ == '__main__':
    # host='0.0.0.0' permet de tester depuis ton téléphone sur le même WiFi
    app.run(host='0.0.0.0', port=5000, debug=True)

#This is a change test
