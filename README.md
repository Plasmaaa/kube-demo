# kube-demo

Petite application web Flask conteneurisee avec Docker.

Auteur : Jason

## Lancer le projet

    docker build -t kube-demo .
        docker run -d -p 5000:5000 --name kube-demo kube-demo

        Application accessible sur http://localhost:5000 (route de sante : /health).
        
