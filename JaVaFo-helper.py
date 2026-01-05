from pathlib import Path
import jpype
import jpype.imports
from jpype import JClass

text = Path("/home/ato/JaVaFo/TRFXSample2.txt").read_text(encoding="utf-8")

jpype.startJVM(classpath=["/home/ato/JaVaFo/extraction/main/main.jar"])

JaVaFoApi = JClass("javafo.api.JaVaFoApi")

out = JaVaFoApi.exec_(1000, text)
print(out)

jpype.shutdownJVM()
