import dash_bootstrap_components as dbc
from PIL import Image
from dash import dcc, html

fh_img_1 = Image.open("assets/1.jpg")
fh_img_2 = Image.open("assets/3.jpg")
fh_img_3 = Image.open("assets/5.jpg")

Ahmet_foto = Image.open("assets/Ahmet.jpeg")
Ledion_foto = Image.open("assets/Ledion.jpeg")
Mariel_foto = Image.open("assets/Mariel.jpeg")
Anis_foto = Image.open("assets/Anis.jpeg")

about_page = html.Div([dbc.Row(dbc.Carousel(
    items=[
        {"key": "1", "src": fh_img_1, "header": "FH: for the future.", "img_style": {"max-height": "700px"}},
        {"key": "2", "src": fh_img_2, "header": "Creative & Complex", "img_style": {"max-height": "700px"}},
        {"key": "3", "src": fh_img_3, "header": "Next Generation", "img_style": {"max-height": "700px"}},
    ],
    controls=True,
    indicators=True,

), ),

    dbc.Row(html.P(
        "This website has been developed as a innovation lab project by FH Technikum Wien students. Technical outcome of this project  Dash and Plotly library's and also practicing with python. Aim of this project for developers, improving their team-working, communication, requirement engineering, time management, planing and documenting skills. Tobias Hildebrandt is the supervisor of this project is.",
        className="about_text")),
    dbc.Row(html.H1("Developers",
                    className="team_tittle")),
    dbc.Row([dbc.Col(html.Img(src=Ahmet_foto, width=3, className="developer_image_1")),
             dbc.Col(html.Img(src=Ledion_foto, width=3, className="developer_image_2")),
             dbc.Col(html.Img(src=Mariel_foto, width=3, className="developer_image_3")),
             dbc.Col(html.Img(src=Anis_foto, width=3, className="developer_image_4"))]),
    dbc.Row([dbc.Col("Ahmet Satilmis", width=3, className="developer_title_1"),
             dbc.Col("Ledion Rejzi", width=3, className="developer_title_2"),
             dbc.Col("Mariel Hajdari", width=3, className="developer_title_3"),
             dbc.Col("Anis Shkembi", width=3, className="developer_title_4")]),
    dbc.Row([dbc.Col(
            "I'm a Computer Science student and want to improve my self in the field of data science. In this project i was the project manager. I was responsible with task distribution, time management, research, code architecture and implementation. I'm able to explain this project into a smallest detail. Our team has a really got communication, it feels great working with my team.",
             width=3, className="developer_text_1"),
        dbc.Col(
            "I have been living in Vienna since February 2020. I'm studying Computer Science at the University of Applied Sciences Technikum Wien and I am very happy to be part of this team.In this project I was responsible for the frontend part, respectively for the graph implementation. My role was also to develope the website with technologies like HTML & CSS."
            , width=3, className="developer_text_2"),
        dbc.Col(
            "My name is Mariel Hajdari and I am proud to be a part of this team. I have been studying at the University of Applied Sciences ‘’Technikum Wien’’ for 2 years and my goal is to specialize in software architecture and development. My role in this project was to create the database and connect it with our project. I also had to make sure that the data was correct and that we could access it any time",width=3, className="developer_text_3"),
        dbc.Col(
            "My name is Anis Shkembi and I’m a student at University of Applied Sciences ‘’Technikum Wien’’since 2019 and I’m studying computer science. I want to specialize in Mobile Development and UI/UX Design. My role for the team in this project was to create the design for the website. I also delt with planning and documentation. I love being part of this team. ",
             width=3, className="developer_text_4"),
        dbc.Row(html.H1("drive safe.", className="drive_safe")),
    ])

], className="about"),


def get_about_page(): return about_page
