from tkinter import *
import psycopg2
import smtplib
from email.message import EmailMessage
from filesecret import senhaEmail
from filesecret import senhaBD

Janela = Tk()
Janela.geometry('700x350')
Janela.config(bg='#E7E7E7')
Janela.title('Realizar cadastro')

def conectar():
    try:
        conexao = psycopg2.connect(
            dbname="userbigdata",
            user="postgres",
            password=senhaBD,
            host="localhost",
            port="5432"
        )
        return conexao
    except psycopg2.Error as e:
        print("Erro ao conectar ao PostgreSQL:", e)
        return None

def inserir_dados(nome, email, cpf, telefone):
    conexao = conectar()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO usuario (nome, email, cpf, telefone) VALUES (%s, %s, %s, %s) RETURNING id", (nome, email, cpf, telefone))
            id_inserido = cursor.fetchone()[0]
            conexao.commit()
            EMAIL_ADDRESS = 'paulocesarmartins2006@gmail.com'
            EMAIL_SENHA = senhaEmail
            
            msg = EmailMessage()
            msg['Subject'] = 'Obrigado'
            msg['From'] = 'paulocesarmartins2006@gmail.com'
            msg['To'] = email
            
            conteudo_email = (
                f'Olá {nome}, seja bem vindo\n\n'
                f'Seu cadastro foi realizado com sucesso em nosso sistema!\n'
            )
            msg.set_content(conteudo_email)
            
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_SENHA)
                smtp.send_message(msg)
            
            # JANELA PRINCIPAL
            Janela.withdraw()
            janelaPrincipal = Toplevel()
            janelaPrincipal.geometry('700x350')
            janelaPrincipal.config(bg='#E7E7E7')
            janelaPrincipal.title('Tela principal')

            #NESSA JANELA FICARAM OS GRAFICOS
            
            label = Label(janelaPrincipal, text='Estoque - Supermercado Canadá')
            label['font'] = 30
            label.config(bg='#E7E7E7')
            label.pack()

            print(id_inserido)
        except psycopg2.Error as e:
            print("Erro ao inserir dados", e)
        finally:
            conexao.close()
    else:
        print("Falha ao conectar ao banco de dados.")

def main():
    title = Label(text='CADASTRAR')
    title['font'] = 40
    title.config(bg='#E7E7E7')
    title.pack(side=TOP,pady=30)
    
    bloco = Frame()
    bloco.config(bg='#E7E7E7')
    bloco.pack()
    
    bloco1 = Frame()
    bloco1.config(bg='#E7E7E7')
    bloco1.pack()
    
    bloco2 = Frame()
    bloco2.config(bg='#E7E7E7')
    bloco2.pack()
    
    bloco3 = Frame()
    bloco3.config(bg='#E7E7E7')
    bloco3.pack()
    
    labelNome = Label(bloco,text='Nome :')
    labelNome.config(bg='#E7E7E7',fg='black')
    labelNome['font'] = 40
    labelNome.pack(side=LEFT,pady=6)
    
    nome = Entry(bloco)
    nome['width'] = 35
    nome.pack(side=LEFT,pady=6)
    
    labelEmail = Label(bloco1,text='Email :')
    labelEmail.config(bg='#E7E7E7',fg='black')
    labelEmail['font'] = 40
    labelEmail.pack(side=LEFT,pady=6)
    
    email = Entry(bloco1)
    email['width'] = 35
    email.pack(side=LEFT,pady=8)
    
    labelCpf = Label(bloco2,text='CPF :')
    labelCpf.config(bg='#E7E7E7')
    labelCpf['font'] = 40
    labelCpf.pack(side=LEFT,pady=6)
    
    cpf = Entry(bloco2)
    cpf['width'] = 35
    cpf.pack(side=LEFT,pady=10)
    
    labelTelefone = Label(bloco3,text='Fone :')
    labelTelefone.config(bg='#E7E7E7')
    labelTelefone['font'] = 40
    labelTelefone.pack(side=LEFT,pady=6)
    
    telefone = Entry(bloco3)
    telefone['width'] = 35
    telefone.pack(side=LEFT,pady=6)

    cadastrar = Button(text='Cadastrar', command=lambda: inserir_dados(nome.get(), email.get(), cpf.get(), telefone.get()))
    cadastrar['width'] = 10
    cadastrar.config(bg='white',fg='black')
    cadastrar['font'] = 10
    cadastrar.pack(pady=10)
    Janela.mainloop()
    
if __name__ == "__main__":
    main()
