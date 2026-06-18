# 🌿 Terê Verde

Plataforma web para consulta de **trilhas, parques, cachoeiras, biodiversidade e eventos ecológicos** de Teresópolis/RJ.

🔗 **Acesse:** https://tere-verde.onrender.com

---

## 👤 Autor

**Wallace Correa**

---

## 📌 Situação Problema

Teresópolis destaca-se pelo seu elevado potencial para o ecoturismo, reunindo importantes áreas naturais e unidades de conservação, como o Parque Nacional da Serra dos Órgãos e o Parque Estadual dos Três Picos.

Apesar dessa riqueza ambiental, o acesso às informações sobre trilhas, parques, eventos, cachoeiras e biodiversidade ainda ocorre de forma fragmentada, dispersa e pouco estruturada, dificultando o planejamento de visitas e a prática de um turismo consciente e organizado.

Diante desse cenário, o **Terê Verde** foi desenvolvido com o objetivo de centralizar essas informações em uma única plataforma digital, proporcionando acesso simplificado, melhor experiência ao usuário e incentivo ao ecoturismo sustentável na região.

---

## 🎯 Objetivo

Criar uma aplicação web que permita:

- Consultar parques e trilhas  
- Visualizar eventos ecológicos  
- Explorar cachoeiras e biodiversidade  
- Verificar se um parque está **🟢 aberto ou 🔴 fechado em tempo real**

---

## 🛠️ Tecnologias Utilizadas

| Camada        | Tecnologia                     | Função |
|--------------|------------------------------|--------|
| Backend      | Django                        | Lógica do sistema |
| API          | Django REST Framework         | Endpoints REST |
| Frontend     | HTML + CSS (Templates)        | Interface |
| Admin        | Django Admin + Jazzmin        | Painel administrativo |
| Banco        | SQLite                        | Armazenamento |
| Deploy       | Render                        | Hospedagem |
| Servidor     | Gunicorn                      | Execução em produção |

---

## ✅ Funcionalidades

- 🌳 **Parques** com descrição e imagens  
- 🥾 **Trilhas** com dificuldade e distância  
- 💧 **Cachoeiras** com ou sem vínculo com parques  
- 🐾 **Biodiversidade** com categorias  
- 📅 **Eventos ecológicos**  
- ⏰ **Status dinâmico** (aberto/fechado por horário)  
- 🔐 **Painel Admin** completo  
- 🎨 Interface moderna com layout em cards  

---

## 📋 Requisitos Funcionais

- RF01 — Exibir página inicial com navegação  
- RF02 — Listar parques com imagens  
- RF03 — Exibir trilhas associadas  
- RF04 — Mostrar eventos  
- RF05 — Apresentar biodiversidade  
- RF06 — Exibir cachoeiras  
- RF07 — Indicar status aberto/fechado  
- RF08 — Navegação entre páginas  

---

## ⚙️ Requisitos Não Funcionais

- Interface intuitiva  
- Tempo de resposta rápido  
- Layout responsivo  
- Alta disponibilidade  
- Código organizado e escalável  
- Compatibilidade com navegadores modernos  

---

## 🚀 Escopo do MVP

Sistema funcional que permite:

- Consulta de informações de ecoturismo  
- Organização centralizada de dados  
- Gerenciamento via painel administrativo  

---

## ❌ Não Implementado

- Login de usuários comuns  
- Sistema de favoritos  
- Comentários/avaliações  
- Integração com mapas  

---

## 📁 Estrutura do Projeto

```text
tere-verde/
│
├── core/           → Models, Views, Templates
├── config/         → Configurações do Django
├── static/         → CSS e imagens
├── media/          → Upload de imagens (não versionado)
│
├── manage.py
├── requirements.txt
├── Procfile
└── README.mD

 ```

---


## 🖥️ Como rodar localmente

```bash
git clone https://github.com/wallace-co/tere-verde.git

cd tere-verde

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## 🔐 Acesso Admin

Para criar um usuário administrador:

```bash
python manage.py createsuperuser
```

Após criar o usuário, acesse:

```text
http://127.0.0.1:8000/admin/
```

🌐 Deploy

https://tere-verde.onrender.com

python manage.py migrate
python manage.py runserver

```
