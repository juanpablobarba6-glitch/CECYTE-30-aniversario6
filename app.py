from datetime import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)

ARCHIVO_RESPUESTAS = "respuestas.txt"


# ============================================================
#  PLANTILLA BASE (estilos, menú y pie de página)
# ============================================================
def plantilla(titulo, contenido):
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{titulo} | CECYTE JALISCO </title>
        <style>
            :root {{
                --fondo: #9effc6;
                --verde: #1a9a28;
                --verde-oscuro: #12741d;
                --oro: #bfa61f;
                --nar: #d96800;
            }}

            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}

            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: var(--fondo);
                color: var(--verde-oscuro);
                min-height: 100vh;
            }}

            /* ---------- NAVEGACION ---------- */
            nav {{
                background: var(--verde-oscuro);
                border-bottom: 4px solid var(--oro);
                padding: 15px 30px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            }}

            .logo {{
                color: white;
                font-size: 22px;
                font-weight: bold;
                letter-spacing: 1px;
            }}

            .menu {{
                display: flex;
                gap: 10px;
            }}

            .menu a {{
                background: var(--nar);
                color: white;
                text-decoration: none;
                padding: 10px 16px;
                border-radius: 8px;
                transition: 0.3s;
                font-weight: 700;
            }}

            .menu a:hover {{
                background: var(--verde);
                color: white;
            }}

            /* ---------- CONTENEDOR ---------- */
            .contenedor {{
                max-width: 900px;
                margin: 40px auto;
                padding: 20px;
            }}

            .card {{
                background: white;
                padding: 30px;
                border: 4px solid var(--oro);
                border-radius: 10px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.08);
                text-align: center;
            }}

            h1 {{
                color: var(--verde-oscuro);
                margin-bottom: 15px;
            }}

            p {{
                color: #4b5563;
                font-size: 17px;
                margin-bottom: 25px;
                line-height: 1.6;
            }}

            /* ---------- INICIO ---------- */
            .esce {{
                display: block;
                width: 320px;
                max-width: 100%;
                height: auto;
                margin: 0 auto 25px;
                border-radius: 10px;
            }}

            .escl {{
                display: block;
                width: 400px;
                max-width: 100%;
                height: auto;
                margin: 0 auto 20px;
            }}

            /* ---------- IMAGENES DE SECCION (Celebremos y Futuro) ---------- */
            .imagen-seccion {{
                display: block;
                width: 100%;
                max-width: 380px;
                height: 210px;
                object-fit: cover;
                border-radius: 12px;
                margin: 0 auto 25px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}

            /* ---------- HISTORIA: ANTES VS AHORA (galeria) ---------- */
            .galeria {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 30px 25px;
                margin-bottom: 35px;
            }}

            .galeria-item img {{
                display: block;
                width: 100%;
                height: 220px;
                object-fit: cover;
                border-radius: 12px;
                margin-bottom: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}

            .galeria-item p {{
                font-size: 16px;
                margin-bottom: 0;
            }}

            /* ---------- HISTORIA: EVENTOS ---------- */
            .eventos {{
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 25px;
                margin-bottom: 25px;
            }}

            .evento {{
                width: 200px;
            }}

            .evento-img {{
                width: 100%;
                height: 130px;
                object-fit: cover;
                border-radius: 10px;
                margin-bottom: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}

            .evento h2 {{
                font-size: 22px;
            }}

            /* ---------- HUELLAS ---------- */
            .oferta-bloque {{
                display: flex;
                align-items: center;
                gap: 25px;
                margin-bottom: 35px;
                text-align: left;
            }}

            .oferta-img {{
                width: 180px;
                height: 180px;
                object-fit: cover;
                border-radius: 12px;
                flex-shrink: 0;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}

            .oferta-texto h2 {{
                font-size: 28px;
                margin-bottom: 10px;
            }}

            .oferta-texto p {{
                font-size: 19px;
                margin-bottom: 0;
            }}

            /* ---------- ORGULLO ---------- */
            .instalaciones {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 50px 80px;
                margin-bottom: 25px;
            }}

            .inst-izq {{
                text-align: left;
            }}

            .inst-der {{
                text-align: right;
            }}

            .inst-cen {{
                grid-column: 1 / -1;
                text-align: center;
            }}

            .inst-item h2 {{
                margin-bottom: 10px;
            }}

            .inst-item p {{
                margin-bottom: 0;
            }}

            .inst-img {{
                display: block;
                width: 100%;
                max-width: 340px;
                height: 230px;
                object-fit: cover;
                border-radius: 10px;
                margin-bottom: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}

            .inst-der .inst-img {{
                margin-left: auto;
            }}

            .inst-cen .inst-img {{
                margin-left: auto;
                margin-right: auto;
            }}

            /* ---------- FUTURO: FORMULARIO ---------- */
            .formulario {{
                margin-top: 35px;
                text-align: center;
            }}

            .formulario h2 {{
                margin-bottom: 15px;
            }}

            .formulario textarea {{
                width: 100%;
                min-height: 140px;
                padding: 12px;
                border: 3px solid var(--oro);
                border-radius: 10px;
                font-family: inherit;
                font-size: 16px;
                color: #4b5563;
                resize: vertical;
                margin-bottom: 15px;
            }}

            .formulario textarea:focus {{
                outline: none;
                border-color: var(--verde);
            }}

            .mensaje-enviado {{
                margin-top: 15px;
                margin-bottom: 0;
                font-weight: bold;
                color: var(--verde-oscuro);
            }}

            /* ---------- BOTONES ---------- */
            .botones {{
                display: flex;
                justify-content: center;
                gap: 12px;
                flex-wrap: wrap;
                margin-top: 20px;
            }}

            .btn {{
                display: inline-block;
                padding: 12px 22px;
                border: none;
                border-radius: 10px;
                text-decoration: none;
                font-family: inherit;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: 0.3s;
                background: var(--verde-oscuro);
                color: white;
            }}

            .btn:hover {{
                background: var(--nar);
                transform: translateY(-2px);
            }}

            footer {{
                background: var(--verde-oscuro);
                text-align: center;
                padding: 25px;
                color: white;
                font-size: 14px;
            }}

            /* ---------- RESPONSIVO ---------- */
            @media (max-width: 600px) {{
                nav {{
                    flex-direction: column;
                    gap: 15px;
                }}

                .menu {{
                    flex-wrap: wrap;
                    justify-content: center;
                }}

                .card {{
                    padding: 20px;
                }}

                h1 {{
                    font-size: 26px;
                }}

                .galeria {{
                    grid-template-columns: 1fr;
                }}

                .oferta-bloque {{
                    flex-direction: column;
                    text-align: center;
                }}

                .instalaciones {{
                    grid-template-columns: 1fr;
                }}

                .inst-izq, .inst-der {{
                    text-align: center;
                }}

                .inst-img, .inst-der .inst-img {{
                    margin-left: auto;
                    margin-right: auto;
                }}
            }}
        </style>
    </head>
    <body>

        <nav>
            <div class="logo">
                CECYTE Jalisco
            </div>

            <div class="menu">
                <a href="/">Inicio</a>
                <a href="/Historia">Historia</a>
                <a href="/Huellas">Huellas</a>
                <a href="/Orgullo">Orgullo</a>
                <a href="/Celebremos">Celebremos</a>
                <a href="/Futuro">Futuro</a>
            </div>
        </nav>

        <main class="contenedor">
            <div class="card">
                {contenido}
            </div>
        </main>

        <footer>
           | © 2026 Mini App | CECYTEJ Ixtlahuacán del Río | Juan Pablo, Jesus Roberto, Emmanuel Alejandro, Joshua Xavier |
        </footer>

    </body>
    </html>
    """


# ============================================================
#  RUTAS
# ============================================================
@app.route('/')
def inicio():
    contenido = """

        <h1>¡Bienvenido a CECYTEJ Plantel 08 Ixtlahuacán del Río!</h1>
        <h1>¡¡CELEBRA CON NOSOTROS ESTE 30 ANIVERSARIO!!</h1>
        <img src="/static/30años.jpg"
        alt="Logo CECYTE Jalisco" class="escl">
        <h2>Formando profesionales técnicos para el futuro de Jalisco</h2>
        <p>
            CECYTE Jalisco impulsa el aprendizaje práctico e innovador para que los estudiantes desarrollen competencias científicas.
        </p>
        <img src="/static/entrada.jpg"
          alt="Estudiantes" class="esce">
        <p>
            Es una institución pública de educación media superior tecnológica comprometida con la formación integral de jóvenes a través de programas de calidad.
            Este es el CECYTEJ Plantel 08 Ixtlahuacán del Río, donde los estudiantes buscan alcanzar el máximo nivel académico a base de sus conocimientos tecnológicos
            y facilitar el rumbo de sus vidas en la carrera técnica elegida.
        </p>

        <div class="botones">
            <a href="/Historia" class="btn btn-principal">Historia</a>
            <a href="/Huellas" class="btn btn-secundario">Huellas</a>
            <a href="/Orgullo" class="btn btn-secundario">Orgullo</a>
            <a href="/Celebremos" class="btn btn-secundario">Celebremos</a>
            <a href="/Futuro" class="btn btn-secundario">Futuro</a>
        </div>
    """
    return plantilla("Inicio", contenido)


@app.route('/Historia')
def Historia():
    # Las imagenes de "Antes vs Ahora" van en la carpeta static/
    # (static/historia1.jpg, static/historia2.jpg, ...).
    # Para agregar otra fila, copia dos bloques <div class="galeria-item">.
    contenido = """
        <h1>NUESTRA HISTORIA</h1>
        <p>CECYTE Ixtlahuacán ha pasado por varios cambios e historias por contar; ha tenido grandes cambios también en sus
        instalaciones, eventos y mejoras que hacen que el plantel se siga manteniendo hasta el día de hoy.</p>

        <h2>Antes (2010-2012) vs Ahora (2026)</h2>
        <div class="galeria">

            <div class="galeria-item">
                <img src="/static/Vgimnasio.jpg" alt="gimnasio antes">
                <p>Antes no se contaba con un gimnasio</p>
            </div>
            <div class="galeria-item">
                <img src="/static/gimnasio.jpg" alt="gimnasio nuevo">
                <p>Actualmente si se cuenta con gimnasio y es de libre acceso</p>
            </div>

            <div class="galeria-item">
                <img src="/static/Vcafeteria.jpg" alt="cafeteria antes">
                <p>Antes no se tenia el domo ni tampoco estaba la estructura de la cafeteria</p>
            </div>
            <div class="galeria-item">
                <img src="/static/cafeteria.jpg" alt="cafeteria actual">
                <p>Actualmente se cuenta con un domo mas solido, una estructura para la cocina y mejores bancas</p>
            </div>

            <div class="galeria-item">
                <img src="/static/Vbiblioteca.jpg" alt="Biblioteca de antes">
                <p>Antes no se contaba con una biblioteca</p>
            </div>
            <div class="galeria-item">
                <img src="/static/biblioteca.jpg" alt="Biblioteca actual">
                <p>Ahora si se cuenta con una y es de libre acceso y puedes buscar los libros con la inormacion que tu requieras en ese momento</p>
            </div>

            <div class="galeria-item">
                <img src="/static/Vcancha.jpg" alt="cancha de antes">
                <p>antes no estaba el domo y tampoco estaban las paredes laterales</p>
            </div>
            <div class="galeria-item">
                <img src="/static/cancha.jpg" alt="cancha actual">
                <p>ahora si tiene un domo y esta esa pared lateral, siendo punto de reunion para la escuela</p>
            </div>

            <div class="galeria-item">
                <img src="/static/Vcartel.jpg" alt="cartel de antes">
                <p>un cartel con el logo antiguo de cecytej y arboles en crecimiento</p>
            </div>
            <div class="galeria-item">
                <img src="/static/cartel.jpg" alt="cartel actual">
                <p>Logo del cecytej actual mas minimalista pero mas directo, arboles ya grandes abundan</p>
            </div>

            <div class="galeria-item">
                <img src="/static/Velectro.jpg" alt="electro de antes">
                <p>el talles de electromecanica hace ya unos años</p>
            </div>
            <div class="galeria-item">
                <img src="/static/electro.jpg" alt="electro actual">
                <p>Taller de electromecanica en la actualidad</p>
            </div>

            <div class="galeria-item">
                <img src="/static/Vlabcom.jpg" alt="labcom de antes">
                <p>Laboratorio de computo de abajo recien inagurado</p>
            </div>
            <div class="galeria-item">
                <img src="/static/labcom.jpg" alt="labcom actual">
                <p>Actualmente es el labratorio principal para los de programacion</p>
            </div>



        </div>

        <h1>ACTIVIDADES Y EVENTOS DEL PLANTEL</h1>
                <p>
                    CECYTEJ Ixtlahuacán del Río realiza numerosas actividades y eventos para los estudiantes, eventos que son tanto internos como externos.
                </p>
                <div class="eventos">
                    <div class="evento">
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZbE3jF0lkOWYUIJH5wOZ9LkxGe3yiMEQ4y8SeAPPeZA&s=10"
                        alt="Desfile 16" class="evento-img">
                        <h2>Desfile del 16 de Septiembre</h2>
                    </div>
                    <div class="evento">
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMO60s1nECo0k1RRDO2ybczYgMUo5JqOD1qrBSPtKAfg&s=10"
                        alt="T Futbol" class="evento-img">
                        <h2>Torneos de Fútbol</h2>
                    </div>
                    <div class="evento">
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxgHMjXtMEVktjUpgoRqhujxaLJxK1LomAd2Rtd2ois1gFLaPFI2vGd6xk&s=10"
                        alt="T Voley" class="evento-img">
                        <h2>Torneos de Vóley</h2>
                    </div>
                    <div class="evento">
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHlQbDITSNGfd-s6UqQ8EYOo_HExQ1644A4VsiNuR-xA&s=10"
                        alt="baile" class="evento-img">
                        <h2>Taller de baile</h2>
                    </div>
                    <div class="evento">
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCIS222IjW7kE2ULHHW2s9eE6X4UmiSjgtDHB7TO3ZGQ&s=10"
                        alt="Muertos" class="evento-img">
                        <h2>Eventos del Día de Muertos</h2>
                    </div>
                </div>


        <div class="botones">
            <a href="/" class="btn btn-secundario">Volver al Inicio</a>
            <a href="/Huellas" class="btn btn-principal">Siguiente ---> Huellas</a>
        </div>
    """
    return plantilla("Historia", contenido)


@app.route('/Huellas')
def Huellas():
    contenido = """

        <h1>VOCES QUE DEJAN HUELLAS</h1>
        <div class="oferta-bloque">
            <div class="oferta-texto">
                <h2>COORDINADOR NICOLAS TOVAR</h2>
                <p>
                    <p>¿En que año se fundo el cecytej 08?</p>
                    1999
                    <p>¿Como fue que se dio la iniciativa para crear este planterl?</p>
                    el presidente de en ese entonces Aaron Tello ayudo para crear este plantel
                    <p>¿cual fue la cantidad aproximada de alumnos de la primera generacion?</p>
                    aproximadamente unos 60 y eran dos grupos pequeños
                </p>
            </div>
        </div>

        <div class="oferta-bloque">
            <div class="oferta-texto">
                <h2>MAESTRA AURELIA ROSTRO</h2>
                <p>
                    <p>¿Que espacios han sido cosntruidos a lo largo de etos 30 años?</p>
                    se han contruido el taller de eletromecanica, la cafeteria, otro edificio, el gabinete psicopedagogico, el gimnasio
                    <p>¿Cuales considera las mejoras mas importantes del plantel?</p>
                    que la hayan equipado mejor, que haya aumentado el numero de alumnos y de docentes, la infraestructura
                    <p>¿Que cambios tecnologicos a experimentado en este plantel?</p>
                    los pizarrones a serpintarrones, computadoras grandes ahora son planas, ahora el internet es inhalambrico.
                </p>
            </div>
        </div>

         <div class="oferta-bloque">
                    <div class="oferta-texto">
                        <h2>MAESTRO JESUS ESTRADA</h2>
                        <p>
                            <p>¿Quienes fueron los primeros directores y docentes?</p>
                            Alberto Montero, Jesus Estrada, Adriana Lozano, Angel, Brito.
                            <p>¿Algun recuerdo?</p>
                            las primeras generaciones se sentian como familia, al ser pocos conviviamos bastante y se festejaban los dias festivos
                            <p>¿Mensaje para las nuevas generaciones?</p>
                            Aprovechen la oportunidad de estar en esta institucion, se a comprobado que despues de graduarse si se nota quien si la ha hehado ganas
                        </p>
                    </div>
                </div>      

        <div class="botones">
            <a href="/Historia" class="btn btn-secundario">Anterior --> Historia</a>
            <a href="/Orgullo" class="btn btn-principal">Siguiente --> Orgullo</a>
            <a href="/" class="btn btn-secundario">Volver al Inicio</a>
        </div>
    """
    return plantilla("Huellas", contenido)


@app.route('/Orgullo')
def Orgullo():
    contenido = """

        <h1>ORGULLO DE CECYTEJ IXTLAHUACÁN DEL RÍO</h1>
        <div class="instalaciones">

            <div class="inst-item inst-izq">
                <h2>---TECNOLOGÍA---</h2>
                <img src="/static/Otecnologias.jpg"
                alt="Tecnología" class="inst-img">
                <p>egresados de cecyte dando charlas para los alumnos actuales</p>
            </div>

            <div class="inst-item inst-der">
                <h2>---CIENCIAS---</h2>
                <img src="/static/Ociencias.jpg"
                alt="Ciencias" class="inst-img">
                <p>ciudad sustentable de la expo ciencias 2024</p>
            </div>

            <div class="inst-item inst-izq">
                <h2>---DEPORTES---</h2>
                <img src="/static/Odeportes.jpg"
                alt="Deportes" class="inst-img">
                <p>torneos de futbol junto a la ula externa de cuquio</p>
            </div>

            <div class="inst-item inst-der">
                <h2>---CULTURA---</h2>
                <img src="/static/Ocultura.jpg"
                alt="Cultura" class="inst-img">
                <p>reciente dia de muertos de cecyte organizada en este año</p>
            </div>

            <div class="inst-item inst-cen">
                <h2>---LOGROS ACADÉMICOS---</h2>
                <img src="/static/Ologros.jpg"
                alt="Logros académicos" class="inst-img">
                <p>alumnos denuevo ingreso listos para hacer su examen</p>
            </div>

        </div>

        <div class="botones">
            <a href="/Huellas" class="btn btn-secundario">Anterior --> Huellas</a>
            <a href="/Celebremos" class="btn btn-secundario">Siguiente --> Celebremos</a>
            <a href="/" class="btn btn-principal">Volver al Inicio</a>
        </div>
    """
    return plantilla("Orgullo", contenido)


@app.route('/Celebremos')
def Celebremos():
    contenido = """

    <h1>¡¡CELEBREMOS JUNTOS ESTE 30 ANIVERSARIO!!</h1>
    <p>Para celebrar este 30 aniversario de CECYTEJ, se tienen propuestas de actividades para que todos juntos
    celebremos estas importantes fechas para la institución.</p>
    <p>Es por eso que tenemos 5 propuestas para poder festejar el 30 aniversario, con actividades recreativas,
    compañerismo y unión entre los estudiantes y docentes.</p>

    <h2>EXPO CIENCIAS</h2>
    <p>Actividad desarrollada por el plantel para hacer una exposición de proyectos realizados por los alumnos y
    presentarlos a otros estudiantes y a otras escuelas invitadas a presenciar el evento.</p>
    <p>En esta expo se presentan trabajos realizados por las carreras del plantel, así como también trabajos de
    ciencias, inglés, humanidades, etc.</p>

    <img src="/static/ciencias.jpg" alt="ciencias" class="imagen-seccion">
    <h2>TORNEOS AMISTOSOS DE DEPORTES</h2>
    <p>Realizar torneos amistosos de deportes de fútbol y voleibol para fortalecer la convivencia e incitar a hacer deporte
    y también fortaleciendo el compañerismo y las mejoras a nivel deportivo.</p>

    <img src="/static/deportes.jpg" alt="deportes" class="imagen-seccion">
    <h2>CONVIVIO</h2>
    <p>Realizar una especie de convivio, ya sea entre salones o entre toda la escuela, para festejar este aniversario
    fortaleciendo la unión y fomentando la convivencia.</p>

    <img src="/static/convivio.jpg" alt="Convivio" class="imagen-seccion">
    <h2>CARACOL</h2>
    <p>Con la reciente llegada de las personas de Cuidémonos Caracol, con la ayuda de ellos se pueden realizar actividades
    para el convivio y la exposición entre los alumnos, torneos de videojuegos, charlas, etc.</p>

    <img src="/static/caracol.jpg" alt="caracol" class="imagen-seccion">
    <h2>DÍA LIBRE</h2>
    <p>Para muchos, lo mejor de estas propuestas: como día festivo interno, dejar el día libre a alumnos y administrativos
    para que se tomen un descanso y un respiro del trabajo.</p>
    <img src="/static/dialibre.jpg" alt="dia libre" class="imagen-seccion">

        <div class="botones">
            <a href="/Orgullo" class="btn btn-secundario">Anterior --> Orgullo</a>
            <a href="/Futuro" class="btn btn-secundario">Siguiente --> Futuro</a>
            <a href="/" class="btn btn-principal">Volver al Inicio</a>
        </div>
    """
    return plantilla("Celebremos", contenido)


@app.route('/Futuro')
def Futuro():
    contenido = """

        <h1>EL FUTURO DE CECYTEJ IXTLAHUACÁN</h1>

        <h2>¿Qué es lo que me gustaría para el futuro del plantel?</h2>

        <p>Es una pregunta que nosotros, los alumnos, nos hacemos muchas veces; queremos muchas cosas
        pero no todo se puede hacer realidad.</p>

        <p>Nos gustaría que en primer semestre se hable un poco más y mejor sobre las carreras que ofrece
        el plantel. No se tiene una visión clara de lo que te puede llegar a esperar más allá de lo que te pueden
        decir otros alumnos; esto ha generado que algunos alumnos hayan terminado arrepentidos de la carrera que eligieron
        o que no sepan bien lo que hacen, haciendo que su rendimiento académico decaiga.</p>

        <img src="/static/estres.jpg" alt="Imagen sobre las carreras del plantel" class="imagen-seccion">

        <p>Algo más que nos gustaría sería un segundo receso. Hay un horario de ocho clases y solo un receso de 
        treinta minutos; el receso comienza después de las tres primeras clases. Nos gustaría que el segundo fuera
        las próximas tres clases después del primer receso. No pedimos un receso largo, puede ser de 15 o 20 minutos
        pero sí otro lapso de descanso para que los estudiantes no se sientan tan frustrados.</p>

        <img src="/static/receso.png" alt="Imagen sobre el segundo receso" class="imagen-seccion">

        <form class="formulario" id="form-futuro">
            <h2>¿Y a ti qué es lo que te gustaría para el futuro del plantel?</h2>
            <textarea id="respuesta" name="respuesta" maxlength="1000"
                      placeholder="Escribe aquí tu respuesta..." required></textarea>
            <button type="submit" class="btn">Enviar respuesta</button>
            <p class="mensaje-enviado" id="mensaje" hidden></p>
        </form>

        <div class="botones">
            <a href="/Celebremos" class="btn btn-secundario">Anterior --> Celebremos</a>
            <a href="/" class="btn btn-principal">Volver al Inicio</a>
        </div>

        <script>
            const form = document.getElementById('form-futuro');
            const caja = document.getElementById('respuesta');
            const mensaje = document.getElementById('mensaje');

            form.addEventListener('submit', async (e) => {
                e.preventDefault();               // evita que la pagina se recargue
                const texto = caja.value.trim();
                if (!texto) return;

                try {
                    const r = await fetch('/enviar-respuesta', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({respuesta: texto})
                    });
                    if (!r.ok) throw new Error();
                    mensaje.textContent = '¡Tu respuesta fue enviada! Gracias por participar.';
                    caja.value = '';
                } catch (err) {
                    mensaje.textContent = 'No se pudo enviar la respuesta. Inténtalo de nuevo.';
                }
                mensaje.hidden = false;
            });
        </script>
    """
    return plantilla("Futuro", contenido)


@app.route('/enviar-respuesta', methods=['POST'])
def enviar_respuesta():
    datos = request.get_json(silent=True) or {}
    texto = str(datos.get("respuesta", "")).strip()[:1000]

    if not texto:
        return jsonify(ok=False), 400

    # Guarda cada respuesta en respuestas.txt con fecha y hora
    with open(ARCHIVO_RESPUESTAS, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now():%Y-%m-%d %H:%M}] {texto}\n")

    return jsonify(ok=True)


if __name__ == '__main__':
    app.run(debug=True)