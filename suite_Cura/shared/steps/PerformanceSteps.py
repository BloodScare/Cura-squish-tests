from PageObjects.CommonPage import PageObject
from PageObjects.CuraPage import Cura
from PageObjects.PerformancePage import Performance

page_object = PageObject()
performance = Performance()
cura = Cura()


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


@Then("I can verify the gcode size of '|any|' is greater than 1kb")
def step(context, file_name):
    file_size = page_object.fileSize(findFile("testdata", file_name))

    context.userData = {}
    context.userData['gcode'] = file_size

    if file_size is not None and file_size > 1:
        test.passes(f"File size: {file_size} KB")
    else:
        test.fail("File size 1 KB or smaller ")


@Then("the line size of '|any|' is printed")
def step(context, file_name):
    lineCount = page_object.lineCount(findFile("testdata", file_name))

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


@When("I move the model |word| x")
def step(context, xPos):
    cura.navigateTo("Edit", "Select All Models")
    cura.moveModel(xPos)


@When("I scale the model to |word|% uniformly")
def step(context, size):
    cura.navigateTo("Edit", "Select All Models")
    cura.scaleModel(size)

@Step("I open POS tool")
def step(context):
    cura.openPOS()

@Step("I modify the setting Infill Density to |any|")
def step(context, infill_density):
    cura.modifyPOSSetting(infill_density)

