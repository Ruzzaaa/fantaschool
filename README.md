il gruppo fantaschool presenta la struttura del lavoro prodotto:

1. Creazione del design delle interfacce grafiche con Python e Tkinter
La prima fase del progetto ha riguardato la progettazione e lo sviluppo delle interfacce grafiche dell’applicazione, utilizzando il modulo Tkinter di Python. L'obiettivo principale era quello di creare un'interfaccia utente intuitiva, accattivante e funzionale, capace di offrire un'esperienza fluida e interattiva.
Durante questa fase, il team ha lavorato su diversi aspetti grafici, tra cui:

La disposizione dei vari elementi grafici all'interno delle finestre dell'applicazione, scegliendo un layout che favorisse la semplicità d'uso e la chiarezza delle informazioni.
L’implementazione di pulsanti, etichette, caselle di testo e altri widget essenziali per l’interazione dell’utente con l’applicazione.
L’ottimizzazione del design per garantire una visualizzazione coerente su diverse dimensioni di schermo.
La gestione degli eventi e delle azioni associate ai vari componenti grafici, assicurando una navigazione fluida tra le diverse sezioni dell’app.
Grazie all’utilizzo di Tkinter, il team ha potuto implementare una GUI modulare e facilmente aggiornabile, in grado di adattarsi alle future esigenze del progetto.

2. Creazione del database con SQL
Dopo aver definito l’interfaccia grafica, il passo successivo è stato quello di progettare e creare un database solido e ben strutturato, capace di memorizzare in modo efficiente tutte le informazioni necessarie al corretto funzionamento dell’applicazione.
La progettazione del database è partita dall'analisi delle necessità del sistema, individuando le tabelle fondamentali e le relazioni tra di esse. Sono stati definiti diversi elementi chiave, tra cui:

Una tabella per la gestione degli utenti, contenente informazioni come nome, cognome, email, classe di appartenenza e punteggio accumulato.
Una tabella dedicata ai voti e ai risultati scolastici, che permette di tracciare le prestazioni degli studenti e di calcolare i punteggi da assegnare nel sistema di Fantaschool.
Una tabella per la gestione dei bonus e dei malus, che tiene traccia dei premi e delle penalizzazioni assegnati agli studenti in base alle loro performance scolastiche.
Meccanismi di sicurezza e vincoli di integrità per garantire che i dati inseriti siano sempre coerenti e privi di errori.
L’utilizzo di SQL ha permesso di realizzare un database efficiente, strutturato in modo da ottimizzare le operazioni di lettura, scrittura e aggiornamento delle informazioni, garantendo al tempo stesso una buona scalabilità per eventuali espansioni future del progetto.


3 Connessione al database 

Grazie a Flask, il team ha potuto sviluppare un’API REST che permette all’interfaccia grafica di inviare richieste HTTP per interagire con il database. L’implementazione ha incluso:

Creazione di endpoint API per operazioni CRUD (Create, Read, Update, Delete) sui dati del database.
Gestione delle richieste HTTP con Flask-Restful per facilitare la comunicazione tra Tkinter e SQL.
Sicurezza e validazione dei dati attraverso meccanismi di autenticazione e autorizzazione per proteggere l’accesso alle informazioni.
Utilizzo di JSON per formattare e trasmettere i dati tra client e server in modo leggibile ed efficiente.
