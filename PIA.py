#  Modulos
#  Cifrado y descifrado
import Menu_cifrado
import Hunter
import EnvioCorreo
import CreateBaseline
#  Librerias Python
import argparse
from socket import *

menu="""\n[E]Escaneo de Puertos flags {-t,-range}
\n[C]Cifrado Cesar {-m, -k, -modo}
\n[H]Hunter {-nombre}
\n[EC] Envio de correo {-usuario, -contrasena, -destinatario, -asunto, -mensaje}
\n[B]Crear un Baseline con Python y PowerShell {-b, -p, -t}"""

#  General
try:
    parser = argparse.ArgumentParser(description="PIA Ciberseguridad")
    parser.add_argument('-o', '--option', metavar='', help=menu)


    #  Escaneo de Puertos
    parser.add_argument('-target', '--target', type=str, metavar='',
                        help='IP a escanear')
    parser.add_argument('-rango', '--rango', metavar='',
                        help='Rango de puertos ej. 50,100')

    #PIA.py -o E -target 192.168.1.80 -rango 120,140

    #  Cifrado Cesar
    parser.add_argument('-m', '--message', metavar='', help='Mensaje a Cifrar')
    parser.add_argument('-k', '--key', metavar='', help='Clave para Cifrar')
    parser.add_argument('-modo', '--modo', metavar='',
                        help='[c]Cifrar, [d]Descifrar, [h]Hackear')

    #  Hunter
    parser.add_argument('-nombre', '--nombre', metavar='',
                        help="Nombre de la Organizacion a investigar")

    #  Envio de correo test.pc.fcfm@gmail.com
    parser.add_argument('-usuario', '--usuario', metavar='',
                        help="Correo del usuario")
    parser.add_argument('-contrasena', '--contrasena', metavar='',
                        help="Contraseña del usuario")
    parser.add_argument('-destinatario', '--destinatario', metavar='',
                    help="Donde se envia el correo")
    parser.add_argument('-asunto', '--asunto', metavar='',
                    help="Asunto del correo")
    parser.add_argument('-mensaje', '--mensaje', metavar='',
                    help="Mensaje del correo")

    #  Hashes
    parser.add_argument('-b', '--baseline', metavar='',
                    help="Specify the resulting baseline file")
    parser.add_argument('-p', '--Path', type= CreateBaseline.ValidatePath,
                    help="Specify the target folder to baseline")
    parser.add_argument('-t', '--tmp', metavar='',
                    help="Specify a temporary result file for the PowerShell Script")

    args = parser.parse_args()

    #  Valores del Argparse
    #  General
    option = args.option
    #  Escaneo de puertos
    target = args.target
    rango = args.rango
    #  Cifrado Cesar
    message = args.message
    key = args.key
    modo = args.modo
    #  Hunter
    organizacion_investigar = args.nombre
    #  Envio de Correo
    user = args.usuario
    contra = args.contrasena
    destinatario = args.destinatario
    asunto = args.asunto
    mensaje = args.mensaje
    #  Hashes
    baselineFile = args.baseline
    targetPath = args.Path
    tmpFile = args.tmp
except:
    option = 0


def Escaneo_Puertos(target, rango):
    ran = rango.split(",")
    #target = argumentalgo3
    #a=int(a)
    t_IP = gethostbyname(target)
    print ('Escaneando la IP: ', t_IP)
    for i in range(int(ran[0]), int(ran[1])+1):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            print ('Puerto %d: Abierto' % (i,))
        s.close()


if __name__ == '__main__':
    if option == "E" and target != None and range != None:
        Escaneo_Puertos(target, rango)
    if option == "C" and message != None:
        if modo == "c" and key != None:
            print("[+] Cifrado Cesar:")
            print("> Mensaje:", message, "\t> Clave:", key)
            print("> Palabra cifrada:")
            Menu_cifrado.cifrar(message, key)
        elif modo == "d" and key != None:
            print("[+] Descifrado Cesar:")
            print("> Mensaje:", message, "\t> Clave:", key)
            print("> Palabra descifrada:")
            Menu_cifrado.descifrar(message, key)
        elif modo == "h" and key == None:
            print("[+] Hackeo a cifrado Cesar:")
            print("> Mensaje:", message)
            print("> Palabra hackeada:")
            Menu_cifrado.hackear(message)
        else:
            print("Faltan opciones por llenar")
    if option == "H" and organizacion_investigar != None:
        Hunter.main(organizacion_investigar)
    if (option == "EC" and user != None and contra != None and
        destinatario != None and asunto != None and mensaje != None):
        EnvioCorreo.Envio_Correo(user, contra, destinatario, asunto, mensaje)
    if (option == "B" and baselineFile != None and
        targetPath != None and tmpFile != None):
        CreateBaseline.main(baselineFile, targetPath, tmpFile)
    if option == "0":
        print("Error al asignar argumentos")
    if (option != "E" and option != "C" and option != "H" and
        option != "EC" and option != "B" and option != 0):
        print("\n[-]Opción no valida\nOpciones correctas"+menu)
