import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

dataframe = pd.read_csv("social_media_user_behavior.csv")

print(dataframe.head())
print(dataframe.dtypes)

print(dataframe.isnull().sum())


print(dataframe["age"].min())
print(dataframe["age"].max())

print(dataframe.groupby('gender')['age'].mean())

sns.boxplot(data=dataframe,x="gender",y="age")
plt.savefig("edades.jpg") 
plt.show() 

plt.clf()

print(dataframe["age"].describe())

print(dataframe["profession"].value_counts())

print(dataframe.groupby("profession")["daily_usage_hours"].agg(["mean"]))


sns.boxplot(data=dataframe,x="profession",y="daily_usage_hours")
plt.savefig("relacion.jpg") 
plt.show()

plt.clf()

print(dataframe["daily_usage_hours"].describe())

print(dataframe["self_reported_mental_health_score"].describe())


sns.scatterplot(data=dataframe,x="daily_usage_hours",y="self_reported_mental_health_score")
plt.savefig("relacion2.jpg") 
plt.show()

plt.clf()


print(dataframe.groupby("gender")[["daily_usage_hours", "self_reported_mental_health_score"]].mean())


print(dataframe.groupby("profession")["self_reported_mental_health_score"].mean())

print(dataframe["primary_platform"].value_counts())

print(dataframe.groupby("primary_platform")["daily_usage_hours"].mean())

print(dataframe.groupby("primary_platform")["sessions_per_day"].mean())

sns.barplot(data=dataframe, x="primary_platform",y="sessions_per_day")
plt.savefig("relacion3.jpg")
plt.show()


plt.clf()

sns.barplot( data=dataframe,x="primary_platform",y="daily_usage_hours",hue="gender")
plt.savefig("relacion4.jpg")
plt.show()

plt.clf()

print(dataframe["preferred_device"].value_counts(normalize=True))

sns.countplot(data=dataframe,x="preferred_device")

plt.savefig("muestra1.jpg")
plt.show()

plt.clf()


print(dataframe.groupby("preferred_device")["daily_usage_hours"].mean())

#hola santi! 
#estoy seguro que aca no se deberia de hacer el cierre teorico, lei e investigue y encontre que tengo que dar como un texto con mis observaciones
#con respecto al EDA elegi este porque me parecio interesante y fue algo que senti que era sencillo para mi nivel, aunque me ayude con clases viejas y los apuntes del cuadernillo
no pude usar todo lo que me enseñaste en el curso (aunque lo intente lo mas que pude)

siento que la base y conocimientos los tengo pero que me falto el ordenar los procesos tal vez 

En el EDA, encontre que el rango minimo de edad que utilizan las redes sociales es de 17 años mientras que el maximo es de 53 años.
aunque no es mucho, predominan tanto el genero masculino como el binario, en cuanto a los profesionales y el uso que le dan.

Destaco que los profesionales como "engineers" son aquellos que le dan mas uso por sobre los "designer", aunque sacando un promedio 
pude descubrir que los investigadores usan un promedio de 3.24 hs mientras que los profesoras usan 2.72 hs.

luego lo lleve del lado de la salud mental, descubriendo que en un promedio entre genero, cantidad de horas de uso y salud mental no habia grandes variaciones acorde 
a lo esperado.

al momento de pasarlo al ambito profesional no encontre grades diferencias aunque pude descubrir que los emprendedores estan por debajo del promedio
predominante con respecto a los otros profesionales y que los investigadores siguen en el "max".

Lo que llamo mi atencion fue que las aplicaciones Instagram y Tiktok predominan por amplia diferencia respecto de otras aplicaciones que se encontraban en la lista 
en las cuales con la ayuda del countplot pude econtrar que el genero binario destaca en el uso de Facebook y que el genero "prefiero no decirlo" no se ve registrado en pinterest

Se entendio que hay 4 aplicaciones que demuestran una diferencia de uso por sobre el resto con un promedio de uso de 5 hs.


