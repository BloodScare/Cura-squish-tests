from pageobjects.common_page import PageObject
from pageobjects.cura_page import Cura
from pageobjects.performance_page import Performance

pageObject = PageObject()
cura = Cura()
performance = Performance()

@Given("Cura is being started in performance mode")
def step(context):
    context.userData = {}
    context.userData['boot'] = performance.trackBootTime()

@Step("the |any| is retrieved from the log")
def step(context, action):
    performance.retrieveFromLog(action)

@Step("the |any| time is printed")
def step(context, action):
    test.passes("{:.2f}".format(context.userData[action]))
    print(action + ' time through GUI: {:.2f}'.format(context.userData[action]))

@When(r"I load |word| |any| in performance mode")
def step(context, word, model):
    context.userData = {}
    
    if word == 'project':
        cura.loadFile(model)
        cura.openFileAsProject()
        context.userData['file load'] = cura.openFileFromSummary(True)
    else:
        context.userData['file load'] = cura.loadFile(model, True)

@Then("I can verify the gcode size is greater than 1kb")
def step(context):
    actualFileSize = pageObject.fileSize(context.userData['gcode'])
    
    if actualFileSize > 1:
        test.passes("File size: %s KB" % actualFileSize)
    else:
        test.fail("File size 1 KB or smaller ")

@Then("the line size of the gcode is printed")
def step(context):
    lineCount = pageObject.lineCount(context.userData['gcode'])
    
    if lineCount > 0:
        test.passes("Line count: %.f" % lineCount)
    else:
        test.fail("Empty or missing file")
    
@Step("I slice the object in performance mode")
def step(context):
    context.userData = {}
    context.userData['slice'] = cura.sliceObject(True)
    
@Step("I save the file as a project in performance mode")
def step(context):
    context.userData = {}
    cura.navigateTo("File", "Save")
    context.userData['writing'] = cura.saveAsProject(True)

@When("I move the model |word| x |word| y")
def step(context, xPos, yPos):
    cura.navigateTo("Edit", "Select All Models")
    cura.moveModel(xPos, yPos)

@When("I scale the model to |word|% uniformly")
def step(context, size):
    cura.navigateTo("Edit", "Select All Models")
    cura.scaleModel(size)
