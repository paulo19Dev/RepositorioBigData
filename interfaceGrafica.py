from tkinter import *
import psycopg2
import smtplib
from email.message import EmailMessage
from filesecret import senhaEmail
from filesecret import senhaBD
from tkinter import messagebox
from PIL import Image, ImageTk

Janela = Tk()
Janela.geometry('1365x735')
Janela.config(bg='#EFEFEF')
Janela.title('TELA DE CADASTRO - SUPERMERCADO CANADA')

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
            
            #Janela.withdraw()
            janelaPrincipal = Toplevel()
            janelaPrincipal.geometry('1365x735')
            janelaPrincipal.config(bg='#E7E7E7')
            janelaPrincipal.title('TELA PRINCIPAL')
            
            title2 = Label(janelaPrincipal, text='Supermercado Canadá',font=("Arial", 20))
            title2.config(bg='#E7E7E7')
            title2.pack(pady=10)

            label = Label(janelaPrincipal, text='CATEGORIAS')
            label['font'] = 30
            label.config(bg='#E7E7E7')
            label.pack(pady=10)
            
            print(id_inserido)
        except psycopg2.Error as e:
            print("Erro ao inserir dados", e)
        finally:
            conexao.close()
    else:
        print("Falha ao conectar ao banco de dados.")
def fundo_Registre():
    image = Image.open('fundo.webp')
    width, height = 500, 650
    image = image.resize((width, height))
    photo = ImageTk.PhotoImage(image)
    label = Label(Janela, image=photo)
    label.image = photo
    x_pos, y_pos = 430, 40
    label.place(x=x_pos, y=y_pos)  
fundo_Registre()

def sucesso_cadastro():
    messagebox.showinfo('Seja bem vindo!', 'Cadastro realizado com sucesso ✔')
    inserir_dados()

def verifica_campos_preenchidos(nome, email, cpf, telefone, user, password):
    if nome.get() == "" or email.get() == "" or cpf.get() == "" or telefone.get() == "" or user.get() == "" or password.get() == "":
        messagebox.showerror('Ops erro!', 'Por favor, preencha todos os campos.')
    elif len(nome.get()) < 2:
        messagebox.showerror('Erro!','Nome com poucos caracteres\n exemplo → jose')
    elif len(email.get()) < 5:
        messagebox.showerror('Erro!','Email com poucos caracteres\n exemplo → jose@gmail.com')
    elif len(cpf.get()) < 11:
        messagebox.showerror('Erro!','Cpf com poucos digitos,\n exemplo → 999.888.444-55')
    elif len(telefone.get()) < 10:
        messagebox.showerror('Erro!','Telefone com poucos digitos,\n exemplo → (62) 9 9999-9999')
    elif len(user.get()) < 3:
        messagebox.showerror('Erro!','Usuário com poucos digitos,\n exemplo → joaozinho')
    elif len(password.get()) < 3:
        messagebox.showerror('Erro!','Senha com poucos digitos,\n quantidade maxima é 4')
    else:
        sucesso_cadastro()
        
def main():
    title = Label(text='CADASTRAR',font=("Arial", 30))
    title.config(bg='#787878',fg='white')
    title.pack(side=TOP,pady=60)
    
    bloco0 = Frame()
    bloco0.config(bg='#787878')
    bloco0.pack()
    
    bloco1 = Frame()
    bloco1.config(bg='#787878')
    bloco1.pack()
    
    bloco1 = Frame()
    bloco1.config(bg='#787878')
    bloco1.pack()
    
    bloco2 = Frame()
    bloco2.config(bg='#787878')
    bloco2.pack()
    
    bloco3 = Frame()
    bloco3.config(bg='#787878')
    bloco3.pack()
    
    bloco4 = Frame()
    bloco4.config(bg='#787878')
    bloco4.pack()
    
    bloco5 = Frame()
    bloco5.config(bg='#787878')
    bloco5.pack()
    
    bloco6 = Frame()
    bloco6.config(bg='#787878')
    bloco6.pack()
    
    bloco7 = Frame()
    bloco7.config(bg='#787878')
    bloco7.pack()
    
    bloco8 = Frame()
    bloco8.config(bg='#787878')
    bloco8.pack()
    
    bloco9 = Frame()
    bloco9.config(bg='#787878')
    bloco9.pack()
    
    bloco10 = Frame()
    bloco10.config(bg='#787878')
    bloco10.pack()
    
    bloco11 = Frame()
    bloco11.config(bg='#787878')
    bloco11.pack()

    labelNome = Label(bloco0,text='Nome',font=("Arial", 15))
    labelNome.config(bg='#787878',fg='white')
    labelNome.pack()
    
    nome = Entry(bloco1,width=30,justify='left')
    nome.config(bg='#CACACA',fg='black')
    nome['font'] = 20
    nome.pack(side=LEFT,pady=6)
        
    labelEmail = Label(bloco2,text='Email',font=("Arial", 15),justify='left')
    labelEmail.config(bg='#787878',fg='white')
    labelEmail.pack(side=LEFT,pady=6)
    
    email = Entry(bloco3,width=30,justify='left')
    email.config(bg='#CACACA',fg='black')
    email['font'] = 20
    email.pack(side=LEFT,pady=6)
    
    labelCpf = Label(bloco4,text='CPF',font=("Arial", 15),justify='left')
    labelCpf.config(bg='#787878',fg='white')
    labelCpf.pack(side=LEFT,pady=6)
    
    cpf = Entry(bloco5,width=30,justify='left')
    cpf.config(bg='#CACACA',fg='black')
    cpf['font'] = 20
    cpf.pack(side=LEFT,pady=6)
    
    labelTelefone = Label(bloco6,text='Telefone',font=("Arial", 15),justify='left')
    labelTelefone.config(bg='#787878',fg='white')
    labelTelefone.pack(side=LEFT,pady=6)
    
    telefone = Entry(bloco7,width=30,justify='left')
    telefone.config(bg='#CACACA',fg='black')
    telefone['font'] = 20
    telefone.pack(side=LEFT,pady=6)

    labelUser = Label(bloco8,text='Usuário',font=("Arial", 15),justify='left')
    labelUser.config(bg='#787878',fg='white')
    labelUser.pack(side=LEFT,pady=6)
    
    user = Entry(bloco9,width=30,justify='left')
    user.config(bg='#CACACA',fg='black')
    user['font'] = 20
    user.pack(side=LEFT,pady=6)
    
    labelPassword = Label(bloco10,text='Senha',font=("Arial", 15),justify='left')
    labelPassword.config(bg='#787878',fg='white')
    labelPassword.pack(side=LEFT,pady=6)
    
    password = Entry(bloco11,width=30,justify='left')
    password.config(bg='#CACACA',fg='black')
    password['font'] = 20
    password.pack(side=LEFT,pady=6)
    
    cadastrar = Button(text='Cadastrar', command=lambda: verifica_campos_preenchidos(nome, email, cpf, telefone, user, password),width=10,font=("Arial", 15))
    cadastrar.config(bg='white',fg='black')
    cadastrar.pack(pady=10)
    
    Janela.mainloop()
if __name__ == "__main__":
    main()
