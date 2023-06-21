import mph
from jpype import JBoolean
from jpype import JClass
import time

def runSimulation(contourFilePath):
    startTime = time.process_time()

    client = mph.start()
    # server = mph.Server(cores=1)

    # create the model.java
    model = client.create("Model")

    model.java.modelPath("./")

    # show Jpype the intention of using an integer with Integer()
    # this has to run after the model is created
    Integer = JClass("java.lang.Integer")

    model.java.label("template.mph")

    model.java.title("Scatterer on Substrate")

    model.java.description(
        "A plane electromagnetic wave is incident on a gold nanoparticle on a dielectric substrate. The absorption and scattering cross sections of the particle are computed for a few different polar and azimuthal angles of incidence."
    )

    model.java.param().set("w", "750[nm]", "Width of physical geometry")
    model.java.param().set("t_pml", "150[nm]", "PML thickness")
    model.java.param().set("h_air", "400[nm]", "Air domain height")
    model.java.param().set("h_subs", "250[nm]", "Substrate domain height")
    model.java.param().set("na", "1", "Refractive index, air")
    model.java.param().set("nb", "1.5", "Refractive index, substrate")
    model.java.param().set("lda0", "532[nm]", "Wavelength")
    model.java.param().set("phi", "0", "Azimuthal angle of incidence in both media")
    model.java.param().set("theta", "0", "Polar angle of incidence in air")
    model.java.param().set(
        "thetab", "asin(na/nb*sin(theta))", "Polar angle in substrate"
    )
    model.java.param().set("I0", "1[MW/m^2]", "Intensity of incident field")
    model.java.param().set("P", "I0*w^2*cos(theta)", "Port power")

    model.java.component().create("comp1", JBoolean(True))

    model.java.component("comp1").geom().create("geom1", 3)

    model.java.result().table().create("tbl1", "Table")
    model.java.result().table().create("tbl2", "Table")
    model.java.result().table().create("tbl3", "Table")
    model.java.result().table().create("tbl4", "Table")
    model.java.result().table().create("tbl5", "Table")
    model.java.result().table().create("tbl6", "Table")
    model.java.result().table().create("tbl7", "Table")
    model.java.result().table().create("tbl8", "Table")
    model.java.result().table().create("tbl9", "Table")
    model.java.result().table().create("tbl10", "Table")
    model.java.result().table().create("tbl11", "Table")
    model.java.result().table().create("tbl12", "Table")
    model.java.result().table().create("tbl13", "Table")

    # model.java.result().create("ImageToCurvePlotGroup", "PlotGroup3D")
    # model.java.result("ImageToCurvePlotGroup").create("surf1", "Surface")

    # model.java.func().create("ImageToCurveImageFunction", "Image")
    # model.java.func("ImageToCurveImageFunction").set("funcname", "i2m_im")
    # model.java.func("ImageToCurveImageFunction").set(
    #     "importedname", "image2model.java_image"
    # )
    # model.java.func("ImageToCurveImageFunction").set("inplace", JBoolean(True))
    # model.java.func("ImageToCurveImageFunction").discardData()
    # model.java.func("ImageToCurveImageFunction").set(
    #     "filename",
    #     "/Users/larsnolden/Library/CloudStorage/OneDrive-UniversityofTwente/plasmonics/rounded_image.png",
    # )
    # model.java.func("ImageToCurveImageFunction").importData()
    # model.java.func("ImageToCurveImageFunction").refresh()

    model.java.component("comp1").mesh().create("mesh1")

    model.java.component("comp1").geom("geom1").create("blk1", "Block")
    model.java.component("comp1").geom("geom1").feature("blk1").set(
        "pos", ["0", "0", "(h_air+t_pml)/2"]
    )
    model.java.component("comp1").geom("geom1").feature("blk1").set("base", "center")
    model.java.component("comp1").geom("geom1").feature("blk1").set(
        "size", ["w+2*t_pml", "w+2*t_pml", "h_air+t_pml"]
    )
    model.java.component("comp1").geom("geom1").feature("blk1").set(
        "layername", ["Layer 1"]
    )
    model.java.component("comp1").geom("geom1").feature("blk1").setIndex(
        "layer", "t_pml", 0
    )
    model.java.component("comp1").geom("geom1").feature("blk1").set(
        "layerleft", JBoolean(True)
    )
    model.java.component("comp1").geom("geom1").feature("blk1").set(
        "layerright", JBoolean(True)
    )
    model.java.component("comp1").geom("geom1").feature("blk1").set(
        "layerfront", JBoolean(True)
    )
    model.java.component("comp1").geom("geom1").feature("blk1").set(
        "layerback", JBoolean(True)
    )
    model.java.component("comp1").geom("geom1").feature("blk1").set(
        "layerbottom", JBoolean(False)
    )
    model.java.component("comp1").geom("geom1").feature("blk1").set(
        "layertop", JBoolean(True)
    )
    model.java.component("comp1").geom("geom1").create("blk2", "Block")
    model.java.component("comp1").geom("geom1").feature("blk2").set(
        "pos", ["0", "0", "-(h_subs+t_pml)/2"]
    )
    model.java.component("comp1").geom("geom1").feature("blk2").set("base", "center")
    model.java.component("comp1").geom("geom1").feature("blk2").set(
        "size", ["w+2*t_pml", "w+2*t_pml", "h_subs+t_pml"]
    )
    model.java.component("comp1").geom("geom1").feature("blk2").set(
        "layername", ["Layer 1"]
    )
    model.java.component("comp1").geom("geom1").feature("blk2").setIndex(
        "layer", "t_pml", 0
    )
    model.java.component("comp1").geom("geom1").feature("blk2").set(
        "layerleft", JBoolean(True)
    )
    model.java.component("comp1").geom("geom1").feature("blk2").set(
        "layerright", JBoolean(True)
    )
    model.java.component("comp1").geom("geom1").feature("blk2").set(
        "layerfront", JBoolean(True)
    )
    model.java.component("comp1").geom("geom1").feature("blk2").set(
        "layerback", JBoolean(True)
    )

    model.java.component("comp1").geom(
        "geom1"
    ).run()  # build geometry up until here to allow the selectors sel_pc1, sel_pc2

    # Selection sel_pc1 (selection_periodic_condition_1)
    model.java.component("comp1").geom("geom1").create("sel_pc1", "ExplicitSelection")
    model.java.component("comp1").geom("geom1").feature("sel_pc1").selection(
        "selection"
    ).init()
    model.java.component("comp1").geom("geom1").feature("sel_pc1").selection(
        "selection"
    ).init(2)
    model.java.component("comp1").geom("geom1").feature("sel_pc1").selection(
        "selection"
    ).set("blk1", 54)
    model.java.component("comp1").geom("geom1").feature("sel_pc1").selection(
        "selection"
    ).set("blk2", 57)
    model.java.component("comp1").geom("geom1").feature("sel_pc1").selection(
        "selection"
    ).set("blk1", 8, 54)
    model.java.component("comp1").geom("geom1").feature("sel_pc1").selection(
        "selection"
    ).set("blk2", 57)
    model.java.component("comp1").geom("geom1").feature("sel_pc1").selection(
        "selection"
    ).set("blk1", 31, 54)
    model.java.component("comp1").geom("geom1").feature("sel_pc1").selection(
        "selection"
    ).set("blk2", 34, 57)

    # Selection sel_pc2
    model.java.component("comp1").geom("geom1").create("sel_pc2", "ExplicitSelection")
    model.java.component("comp1").geom("geom1").feature("sel_pc2").selection(
        "selection"
    ).init()
    model.java.component("comp1").geom("geom1").feature("sel_pc2").selection(
        "selection"
    ).init(2)
    model.java.component("comp1").geom("geom1").feature("sel_pc2").selection(
        "selection"
    ).set("blk1", 39)
    model.java.component("comp1").geom("geom1").feature("sel_pc2").selection(
        "selection"
    ).set("blk2", 42)
    model.java.component("comp1").geom("geom1").feature("sel_pc2").selection(
        "selection"
    ).set("blk1", 32, 39)
    model.java.component("comp1").geom("geom1").feature("sel_pc2").selection(
        "selection"
    ).set("blk2", 35, 42)

    # Selection sel_ftri1 (selection free tiangular 1)
    model.java.component("comp1").geom("geom1").create("sel_ftri1", "ExplicitSelection")
    model.java.component("comp1").geom("geom1").feature("sel_ftri1").selection(
        "selection"
    ).init(2)
    model.java.component("comp1").geom("geom1").feature("sel_ftri1").selection(
        "selection"
    ).set("blk1", 31, 32, 39, 54)
    model.java.component("comp1").geom("geom1").feature("sel_ftri1").selection(
        "selection"
    ).set("blk2", 34, 35, 42, 57)

    # selection air
    model.java.component("comp1").geom("geom1").create("air", "ExplicitSelection")
    model.java.component("comp1").geom("geom1").feature("air").selection(
        "selection"
    ).set("blk1", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)

    # selection substrate
    model.java.component("comp1").geom("geom1").create("substrate", "ExplicitSelection")
    model.java.component("comp1").geom("geom1").feature("substrate").selection(
        "selection"
    ).set("blk2", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)

    model.java.component("comp1").geom("geom1").create("wp1", "WorkPlane")
    model.java.component("comp1").geom("geom1").feature("wp1").set(
        "unite", JBoolean(True)
    )
    model.java.component("comp1").geom("geom1").feature("wp1").geom().create(
        "image_ic", "InterpolationCurve"
    )
    model.java.component("comp1").geom("geom1").feature("wp1").geom().feature(
        "image_ic"
    ).set("source", "file")
    model.java.component("comp1").geom("geom1").feature("wp1").geom().feature(
        "image_ic"
    ).set(
        "filename",
        contourFilePath,
    )
    model.java.component("comp1").geom("geom1").feature("wp1").geom().feature(
        "image_ic"
    ).importData()
    model.java.component("comp1").geom("geom1").feature("wp1").geom().feature(
        "image_ic"
    ).set("struct", "sectionwise")
    model.java.component("comp1").geom("geom1").feature("wp1").geom().feature(
        "image_ic"
    ).set("type", "solid")
    model.java.component("comp1").geom("geom1").feature("wp1").geom().feature(
        "image_ic"
    ).set("rtol", 0.001)
    model.java.component("comp1").geom("geom1").feature("wp1").geom().create(
        "scale_ic", "Scale"
    )
    model.java.component("comp1").geom("geom1").feature("wp1").geom().feature(
        "scale_ic"
    ).setIndex("factor", "5.000000000000001E-7/2400", 0)
    model.java.component("comp1").geom("geom1").feature("wp1").geom().feature(
        "scale_ic"
    ).selection("input").set("image_ic")
    model.java.component("comp1").geom("geom1").create("ext1", "Extrude")
    model.java.component("comp1").geom("geom1").feature("ext1").setIndex(
        "distance", "20[nm]", 0
    )
    model.java.component("comp1").geom("geom1").feature("ext1").selection("input").set(
        "wp1"
    )
    model.java.component("comp1").geom("geom1").create("mov2", "Move")
    model.java.component("comp1").geom("geom1").feature("mov2").label("Nanoparticle")

    model.java.component("comp1").geom("geom1").feature("mov2").set(
        "selresult", JBoolean(True)
    )
    model.java.component("comp1").geom("geom1").feature("mov2").set(
        "displx", "-250[nm]"
    )
    model.java.component("comp1").geom("geom1").feature("mov2").set(
        "disply", "-250[nm]"
    )
    model.java.component("comp1").geom("geom1").feature("mov2").selection("input").set(
        "ext1"
    )

    model.java.component("comp1").geom("geom1").run()
    model.java.component("comp1").geom("geom1").run("fin")

    model.java.component("comp1").selection().create("sel1", "Explicit")
    model.java.component("comp1").selection("sel1").set(18, 19)
    model.java.component("comp1").selection().create("com1", "Complement")
    model.java.component("comp1").selection().create("sel2", "Explicit")
    model.java.component("comp1").selection("sel2").set(1, 2, 3)
    model.java.component("comp1").selection().create("sel3", "Explicit")
    model.java.component("comp1").selection("sel3").geom("geom1", 3, 2, ["exterior"])
    model.java.component("comp1").selection("sel3").set(1, 2, 3, 4, 5, 6, 7)
    model.java.component("comp1").selection("sel1").label("Physical Domains")
    model.java.component("comp1").selection("com1").label("PML Domains")
    model.java.component("comp1").selection("com1").set("input", ["sel1"])

    model.java.component("comp1").variable().create("var1")
    model.java.component("comp1").variable("var1").set("ewfd.Ex", "0")
    model.java.component("comp1").variable("var1").set("ewfd.Ey", "0")
    model.java.component("comp1").variable("var1").set("ewfd.Ez", "0")
    model.java.component("comp1").variable("var1").selection().named("com1")
    model.java.component("comp1").variable().create("var2")
    model.java.component("comp1").variable("var2").set("E0x", "-sin(phi)")
    model.java.component("comp1").variable("var2").set("E0y", "cos(phi)")
    model.java.component("comp1").variable("var2").selection().geom("geom1", 2)
    model.java.component("comp1").variable("var2").selection().set(62, 68)
    model.java.component("comp1").variable().create("var3")
    model.java.component("comp1").variable("var3").set(
        "nrelPoav",
        "nx*ewfd2.relPoavx+ny*ewfd2.relPoavy+nz*ewfd2.relPoavz",
        "Relative normal Poynting flux",
    )
    model.java.component("comp1").variable("var3").set(
        "sigma_sc", "intop_surf(nrelPoav)/I0", "Scattering cross section"
    )
    model.java.component("comp1").variable("var3").set(
        "sigma_abs", "intop_vol(ewfd2.Qh)/I0", "Absorption cross section"
    )
    model.java.component("comp1").variable("var3").set(
        "sigma_ext", "sigma_sc+sigma_abs", "Extinction cross section"
    )

    model.java.component("comp1").view("view1").clip().create("plane1", "ClipPlane")

    model.java.component("comp1").material().create("mat1", "Common")
    model.java.component("comp1").material().create("mat2", "Common")
    model.java.component("comp1").material().create("mat3", "Common")
    model.java.component("comp1").material("mat1").selection().named("geom1_air")
    model.java.component("comp1").material("mat1").propertyGroup().create(
        "RefractiveIndex", "Refractive index"
    )
    model.java.component("comp1").material("mat2").selection().named("geom1_substrate")
    model.java.component("comp1").material("mat2").propertyGroup().create(
        "RefractiveIndex", "Refractive index"
    )
    model.java.component("comp1").material("mat3").selection().named("geom1_mov2_dom")
    model.java.component("comp1").material("mat3").propertyGroup().create(
        "RefractiveIndex", "Refractive index"
    )
    model.java.component("comp1").material("mat3").propertyGroup(
        "RefractiveIndex"
    ).func().create("int1", "Interpolation")
    model.java.component("comp1").material("mat3").propertyGroup(
        "RefractiveIndex"
    ).func().create("int2", "Interpolation")

    model.java.component("comp1").cpl().create("intop1", "Integration")
    model.java.component("comp1").cpl().create("intop2", "Integration")
    model.java.component("comp1").cpl("intop1").selection().named("geom1_mov2_dom")
    model.java.component("comp1").cpl("intop2").selection().named("sel3")

    model.java.component("comp1").coordSystem().create("pml1", "PML")
    model.java.component("comp1").coordSystem("pml1").selection().named("com1")

    model.java.component("comp1").physics().create(
        "ewfd", "ElectromagneticWavesFrequencyDomain", "geom1"
    )
    model.java.component("comp1").physics("ewfd").selection().set(18, 19)
    model.java.component("comp1").physics("ewfd").create(
        "wee2", "WaveEquationElectric", 3
    )
    model.java.component("comp1").physics("ewfd").feature("wee2").selection().named(
        "geom1_mov2_dom"
    )
    model.java.component("comp1").physics("ewfd").create("port1", "Port", 2)
    model.java.component("comp1").physics("ewfd").feature("port1").selection().set(68)
    model.java.component("comp1").physics("ewfd").create("port2", "Port", 2)
    model.java.component("comp1").physics("ewfd").feature("port2").selection().set(62)
    model.java.component("comp1").physics("ewfd").create("pc1", "PeriodicCondition", 2)
    model.java.component("comp1").physics("ewfd").feature("pc1").selection().named(
        "geom1_sel_pc1"
    )
    model.java.component("comp1").physics("ewfd").create("pc2", "PeriodicCondition", 2)
    model.java.component("comp1").physics("ewfd").feature("pc2").selection().named(
        "geom1_sel_pc2"
    )
    model.java.component("comp1").physics().create(
        "ewfd2", "ElectromagneticWavesFrequencyDomain", "geom1"
    )

    model.java.component("comp1").mesh("mesh1").create("size1", "Size")
    model.java.component("comp1").mesh("mesh1").create("size2", "Size")
    model.java.component("comp1").mesh("mesh1").create("ftri1", "FreeTri")
    model.java.component("comp1").mesh("mesh1").create("ftet1", "FreeTet")
    model.java.component("comp1").mesh("mesh1").create("swe1", "Sweep")
    model.java.component("comp1").mesh("mesh1").feature("size1").selection().named(
        "geom1_mov2_dom"
    )
    model.java.component("comp1").mesh("mesh1").feature("size2").selection().geom(
        "geom1", 3
    )
    model.java.component("comp1").mesh("mesh1").feature("size2").selection().set(18)
    model.java.component("comp1").mesh("mesh1").feature("ftri1").selection().named(
        "geom1_sel_ftri1"
    )
    model.java.component("comp1").mesh("mesh1").feature("swe1").create(
        "dis1", "Distribution"
    )

    model.java.result().table("tbl1").comments("Global Evaluation 1")
    model.java.result().table("tbl2").comments("Global Evaluation 2")
    model.java.result().table("tbl3").comments("EnhancementFactorGloabl")
    model.java.result().table("tbl4").comments("EnhancementFactorGloabl")
    model.java.result().table("tbl5").comments("EnhancementFactorGloabl")
    model.java.result().table("tbl6").comments("EnhancementFactor")
    model.java.result().table("tbl7").comments("Absorped Power")
    model.java.result().table("tbl8").comments("Absorped Power")
    model.java.result().table("tbl9").comments("Absorped Power")
    model.java.result().table("tbl10").comments("Absorped Power")
    model.java.result().table("tbl11").comments("Absorped Power")
    model.java.result().table("tbl12").comments("Volume Integration 1")
    model.java.result().table("tbl13").comments("LightToHeat")

    model.java.component("comp1").view("view1").set("transparency", JBoolean(True))
    # model.java.component("comp1").view("view1").clip("plane1").set(
    #     "translationamount", 9.710000000000004e-8
    # )
    # model.java.component("comp1").view("view1").clip("plane1").set(
    #     "position", [-1.7998105605876447e-7, 0, 7.500000000000008e-8]
    # )
    # model.java.component("comp1").view("view1").clip("plane1").set(
    #     "orientationaxes", [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]
    # )
    model.java.component("comp1").view("view2").axis().set(
        "xmin", -9.512755809737428e-7
    )
    model.java.component("comp1").view("view2").axis().set("xmax", 9.512755809737428e-7)
    model.java.component("comp1").view("view2").axis().set(
        "ymin", -5.775000317953527e-7
    )
    model.java.component("comp1").view("view2").axis().set("ymax", 5.775000317953527e-7)

    model.java.component("comp1").material("mat1").label("Air")
    model.java.component("comp1").material("mat1").propertyGroup("RefractiveIndex").set(
        "n", ["na", "0", "0", "0", "na", "0", "0", "0", "na"]
    )
    model.java.component("comp1").material("mat2").label("Substrate")
    model.java.component("comp1").material("mat2").propertyGroup("RefractiveIndex").set(
        "n", ["nb", "0", "0", "0", "nb", "0", "0", "0", "nb"]
    )
    model.java.component("comp1").material("mat3").label(
        "Au (Gold) (Rakic et al. 1998: Brendel-Bormann model.java n,k 0.248-6.20 um)"
    )
    model.java.component("comp1").material("mat3").propertyGroup(
        "RefractiveIndex"
    ).func("int1").set("funcname", "nr")
    model.java.component("comp1").material("mat3").propertyGroup(
        "RefractiveIndex"
    ).func("int1").set(
        "table",
        [
            ["2.4797e-01", "1.4943e+00"],
            ["2.5201e-01", "1.5158e+00"],
            ["2.5612e-01", "1.5382e+00"],
            ["2.6030e-01", "1.5611e+00"],
            ["2.6454e-01", "1.5844e+00"],
            ["2.6886e-01", "1.6078e+00"],
            ["2.7324e-01", "1.6306e+00"],
            ["2.7770e-01", "1.6527e+00"],
            ["2.8222e-01", "1.6733e+00"],
            ["2.8683e-01", "1.6921e+00"],
            ["2.9150e-01", "1.7085e+00"],
            ["2.9626e-01", "1.7220e+00"],
            ["3.0109e-01", "1.7322e+00"],
            ["3.0600e-01", "1.7387e+00"],
            ["3.1099e-01", "1.7411e+00"],
            ["3.1606e-01", "1.7391e+00"],
            ["3.2121e-01", "1.7327e+00"],
            ["3.2645e-01", "1.7219e+00"],
            ["3.3177e-01", "1.7071e+00"],
            ["3.3718e-01", "1.6887e+00"],
            ["3.4268e-01", "1.6677e+00"],
            ["3.4827e-01", "1.6452e+00"],
            ["3.5395e-01", "1.6224e+00"],
            ["3.5972e-01", "1.6006e+00"],
            ["3.6559e-01", "1.5810e+00"],
            ["3.7155e-01", "1.5645e+00"],
            ["3.7761e-01", "1.5515e+00"],
            ["3.8377e-01", "1.5419e+00"],
            ["3.9002e-01", "1.5351e+00"],
            ["3.9638e-01", "1.5301e+00"],
            ["4.0285e-01", "1.5255e+00"],
            ["4.0942e-01", "1.5196e+00"],
            ["4.1609e-01", "1.5107e+00"],
            ["4.2288e-01", "1.4971e+00"],
            ["4.2977e-01", "1.4771e+00"],
            ["4.3678e-01", "1.4493e+00"],
            ["4.4390e-01", "1.4126e+00"],
            ["4.5114e-01", "1.3661e+00"],
            ["4.5850e-01", "1.3095e+00"],
            ["4.6598e-01", "1.2427e+00"],
            ["4.7358e-01", "1.1664e+00"],
            ["4.8130e-01", "1.0821e+00"],
            ["4.8915e-01", "9.9182e-01"],
            ["4.9712e-01", "8.9849e-01"],
            ["5.0523e-01", "8.0543e-01"],
            ["5.1347e-01", "7.1590e-01"],
            ["5.2184e-01", "6.3260e-01"],
            ["5.3035e-01", "5.5731e-01"],
            ["5.3900e-01", "4.9085e-01"],
            ["5.4779e-01", "4.3326e-01"],
            ["5.5672e-01", "3.8405e-01"],
            ["5.6580e-01", "3.4242e-01"],
            ["5.7503e-01", "3.0751e-01"],
            ["5.8440e-01", "2.7843e-01"],
            ["5.9393e-01", "2.5437e-01"],
            ["6.0362e-01", "2.3457e-01"],
            ["6.1346e-01", "2.1841e-01"],
            ["6.2346e-01", "2.0533e-01"],
            ["6.3363e-01", "1.9487e-01"],
            ["6.4396e-01", "1.8664e-01"],
            ["6.5446e-01", "1.8030e-01"],
            ["6.6514e-01", "1.7558e-01"],
            ["6.7598e-01", "1.7227e-01"],
            ["6.8701e-01", "1.7016e-01"],
            ["6.9821e-01", "1.6911e-01"],
            ["7.0959e-01", "1.6897e-01"],
            ["7.2117e-01", "1.6966e-01"],
            ["7.3292e-01", "1.7107e-01"],
            ["7.4488e-01", "1.7313e-01"],
            ["7.5702e-01", "1.7577e-01"],
            ["7.6937e-01", "1.7895e-01"],
            ["7.8191e-01", "1.8262e-01"],
            ["7.9466e-01", "1.8675e-01"],
            ["8.0762e-01", "1.9129e-01"],
            ["8.2079e-01", "1.9621e-01"],
            ["8.3418e-01", "2.0151e-01"],
            ["8.4778e-01", "2.0715e-01"],
            ["8.6160e-01", "2.1311e-01"],
            ["8.7565e-01", "2.1938e-01"],
            ["8.8993e-01", "2.2594e-01"],
            ["9.0445e-01", "2.3278e-01"],
            ["9.1919e-01", "2.3989e-01"],
            ["9.3418e-01", "2.4725e-01"],
            ["9.4942e-01", "2.5486e-01"],
            ["9.6490e-01", "2.6271e-01"],
            ["9.8063e-01", "2.7079e-01"],
            ["9.9662e-01", "2.7909e-01"],
            ["1.0129e+00", "2.8761e-01"],
            ["1.0294e+00", "2.9634e-01"],
            ["1.0462e+00", "3.0528e-01"],
            ["1.0632e+00", "3.1442e-01"],
            ["1.0806e+00", "3.2376e-01"],
            ["1.0982e+00", "3.3329e-01"],
            ["1.1161e+00", "3.4302e-01"],
            ["1.1343e+00", "3.5293e-01"],
            ["1.1528e+00", "3.6304e-01"],
            ["1.1716e+00", "3.7334e-01"],
            ["1.1907e+00", "3.8382e-01"],
            ["1.2101e+00", "3.9449e-01"],
            ["1.2299e+00", "4.0535e-01"],
            ["1.2499e+00", "4.1641e-01"],
            ["1.2703e+00", "4.2765e-01"],
            ["1.2910e+00", "4.3909e-01"],
            ["1.3121e+00", "4.5072e-01"],
            ["1.3335e+00", "4.6256e-01"],
            ["1.3552e+00", "4.7459e-01"],
            ["1.3773e+00", "4.8684e-01"],
            ["1.3998e+00", "4.9930e-01"],
            ["1.4226e+00", "5.1198e-01"],
            ["1.4458e+00", "5.2488e-01"],
            ["1.4694e+00", "5.3801e-01"],
            ["1.4933e+00", "5.5138e-01"],
            ["1.5177e+00", "5.6499e-01"],
            ["1.5424e+00", "5.7885e-01"],
            ["1.5676e+00", "5.9297e-01"],
            ["1.5931e+00", "6.0736e-01"],
            ["1.6191e+00", "6.2203e-01"],
            ["1.6455e+00", "6.3699e-01"],
            ["1.6723e+00", "6.5224e-01"],
            ["1.6996e+00", "6.6780e-01"],
            ["1.7273e+00", "6.8368e-01"],
            ["1.7555e+00", "6.9989e-01"],
            ["1.7841e+00", "7.1645e-01"],
            ["1.8132e+00", "7.3336e-01"],
            ["1.8428e+00", "7.5065e-01"],
            ["1.8728e+00", "7.6831e-01"],
            ["1.9034e+00", "7.8638e-01"],
            ["1.9344e+00", "8.0486e-01"],
            ["1.9660e+00", "8.2377e-01"],
            ["1.9980e+00", "8.4313e-01"],
            ["2.0306e+00", "8.6294e-01"],
            ["2.0637e+00", "8.8324e-01"],
            ["2.0974e+00", "9.0404e-01"],
            ["2.1316e+00", "9.2535e-01"],
            ["2.1663e+00", "9.4720e-01"],
            ["2.2016e+00", "9.6961e-01"],
            ["2.2375e+00", "9.9259e-01"],
            ["2.2740e+00", "1.0162e+00"],
            ["2.3111e+00", "1.0404e+00"],
            ["2.3488e+00", "1.0652e+00"],
            ["2.3871e+00", "1.0907e+00"],
            ["2.4260e+00", "1.1169e+00"],
            ["2.4656e+00", "1.1438e+00"],
            ["2.5058e+00", "1.1715e+00"],
            ["2.5467e+00", "1.1999e+00"],
            ["2.5882e+00", "1.2291e+00"],
            ["2.6304e+00", "1.2592e+00"],
            ["2.6733e+00", "1.2901e+00"],
            ["2.7169e+00", "1.3219e+00"],
            ["2.7612e+00", "1.3545e+00"],
            ["2.8062e+00", "1.3882e+00"],
            ["2.8520e+00", "1.4228e+00"],
            ["2.8985e+00", "1.4584e+00"],
            ["2.9457e+00", "1.4951e+00"],
            ["2.9938e+00", "1.5328e+00"],
            ["3.0426e+00", "1.5717e+00"],
            ["3.0922e+00", "1.6117e+00"],
            ["3.1426e+00", "1.6529e+00"],
            ["3.1939e+00", "1.6954e+00"],
            ["3.2460e+00", "1.7391e+00"],
            ["3.2989e+00", "1.7842e+00"],
            ["3.3527e+00", "1.8306e+00"],
            ["3.4074e+00", "1.8784e+00"],
            ["3.4629e+00", "1.9277e+00"],
            ["3.5194e+00", "1.9785e+00"],
            ["3.5768e+00", "2.0308e+00"],
            ["3.6351e+00", "2.0847e+00"],
            ["3.6944e+00", "2.1403e+00"],
            ["3.7546e+00", "2.1976e+00"],
            ["3.8159e+00", "2.2566e+00"],
            ["3.8781e+00", "2.3175e+00"],
            ["3.9413e+00", "2.3802e+00"],
            ["4.0056e+00", "2.4449e+00"],
            ["4.0709e+00", "2.5116e+00"],
            ["4.1373e+00", "2.5803e+00"],
            ["4.2048e+00", "2.6511e+00"],
            ["4.2733e+00", "2.7242e+00"],
            ["4.3430e+00", "2.7995e+00"],
            ["4.4138e+00", "2.8771e+00"],
            ["4.4858e+00", "2.9572e+00"],
            ["4.5589e+00", "3.0397e+00"],
            ["4.6333e+00", "3.1247e+00"],
            ["4.7088e+00", "3.2124e+00"],
            ["4.7856e+00", "3.3028e+00"],
            ["4.8637e+00", "3.3960e+00"],
            ["4.9430e+00", "3.4921e+00"],
            ["5.0236e+00", "3.5911e+00"],
            ["5.1055e+00", "3.6932e+00"],
            ["5.1888e+00", "3.7985e+00"],
            ["5.2734e+00", "3.9069e+00"],
            ["5.3594e+00", "4.0187e+00"],
            ["5.4468e+00", "4.1340e+00"],
            ["5.5356e+00", "4.2528e+00"],
            ["5.6258e+00", "4.3752e+00"],
            ["5.7176e+00", "4.5013e+00"],
            ["5.8108e+00", "4.6314e+00"],
            ["5.9056e+00", "4.7653e+00"],
            ["6.0019e+00", "4.9034e+00"],
            ["6.0997e+00", "5.0456e+00"],
            ["6.1992e+00", "5.1922e+00"],
        ],
    )
    model.java.component("comp1").material("mat3").propertyGroup(
        "RefractiveIndex"
    ).func("int1").set("fununit", ["1"])
    model.java.component("comp1").material("mat3").propertyGroup(
        "RefractiveIndex"
    ).func("int1").set("argunit", ["um"])
    model.java.component("comp1").material("mat3").propertyGroup(
        "RefractiveIndex"
    ).func("int2").set("funcname", "ni")
    model.java.component("comp1").material("mat3").propertyGroup(
        "RefractiveIndex"
    ).func("int2").set(
        "table",
        [
            ["2.4797e-01", "1.9575e+00"],
            ["2.5201e-01", "1.9594e+00"],
            ["2.5612e-01", "1.9605e+00"],
            ["2.6030e-01", "1.9604e+00"],
            ["2.6454e-01", "1.9587e+00"],
            ["2.6886e-01", "1.9551e+00"],
            ["2.7324e-01", "1.9494e+00"],
            ["2.7770e-01", "1.9414e+00"],
            ["2.8222e-01", "1.9312e+00"],
            ["2.8683e-01", "1.9188e+00"],
            ["2.9150e-01", "1.9042e+00"],
            ["2.9626e-01", "1.8879e+00"],
            ["3.0109e-01", "1.8700e+00"],
            ["3.0600e-01", "1.8512e+00"],
            ["3.1099e-01", "1.8319e+00"],
            ["3.1606e-01", "1.8128e+00"],
            ["3.2121e-01", "1.7946e+00"],
            ["3.2645e-01", "1.7784e+00"],
            ["3.3177e-01", "1.7648e+00"],
            ["3.3718e-01", "1.7548e+00"],
            ["3.4268e-01", "1.7490e+00"],
            ["3.4827e-01", "1.7479e+00"],
            ["3.5395e-01", "1.7516e+00"],
            ["3.5972e-01", "1.7597e+00"],
            ["3.6559e-01", "1.7714e+00"],
            ["3.7155e-01", "1.7856e+00"],
            ["3.7761e-01", "1.8007e+00"],
            ["3.8377e-01", "1.8152e+00"],
            ["3.9002e-01", "1.8276e+00"],
            ["3.9638e-01", "1.8366e+00"],
            ["4.0285e-01", "1.8413e+00"],
            ["4.0942e-01", "1.8411e+00"],
            ["4.1609e-01", "1.8362e+00"],
            ["4.2288e-01", "1.8268e+00"],
            ["4.2977e-01", "1.8140e+00"],
            ["4.3678e-01", "1.7988e+00"],
            ["4.4390e-01", "1.7829e+00"],
            ["4.5114e-01", "1.7681e+00"],
            ["4.5850e-01", "1.7567e+00"],
            ["4.6598e-01", "1.7509e+00"],
            ["4.7358e-01", "1.7532e+00"],
            ["4.8130e-01", "1.7661e+00"],
            ["4.8915e-01", "1.7916e+00"],
            ["4.9712e-01", "1.8312e+00"],
            ["5.0523e-01", "1.8852e+00"],
            ["5.1347e-01", "1.9530e+00"],
            ["5.2184e-01", "2.0328e+00"],
            ["5.3035e-01", "2.1222e+00"],
            ["5.3900e-01", "2.2188e+00"],
            ["5.4779e-01", "2.3201e+00"],
            ["5.5672e-01", "2.4245e+00"],
            ["5.6580e-01", "2.5305e+00"],
            ["5.7503e-01", "2.6370e+00"],
            ["5.8440e-01", "2.7434e+00"],
            ["5.9393e-01", "2.8493e+00"],
            ["6.0362e-01", "2.9545e+00"],
            ["6.1346e-01", "3.0587e+00"],
            ["6.2346e-01", "3.1621e+00"],
            ["6.3363e-01", "3.2645e+00"],
            ["6.4396e-01", "3.3662e+00"],
            ["6.5446e-01", "3.4671e+00"],
            ["6.6514e-01", "3.5675e+00"],
            ["6.7598e-01", "3.6674e+00"],
            ["6.8701e-01", "3.7669e+00"],
            ["6.9821e-01", "3.8661e+00"],
            ["7.0959e-01", "3.9653e+00"],
            ["7.2117e-01", "4.0644e+00"],
            ["7.3292e-01", "4.1635e+00"],
            ["7.4488e-01", "4.2629e+00"],
            ["7.5702e-01", "4.3625e+00"],
            ["7.6937e-01", "4.4624e+00"],
            ["7.8191e-01", "4.5627e+00"],
            ["7.9466e-01", "4.6635e+00"],
            ["8.0762e-01", "4.7649e+00"],
            ["8.2079e-01", "4.8669e+00"],
            ["8.3418e-01", "4.9695e+00"],
            ["8.4778e-01", "5.0729e+00"],
            ["8.6160e-01", "5.1770e+00"],
            ["8.7565e-01", "5.2820e+00"],
            ["8.8993e-01", "5.3878e+00"],
            ["9.0445e-01", "5.4946e+00"],
            ["9.1919e-01", "5.6024e+00"],
            ["9.3418e-01", "5.7111e+00"],
            ["9.4942e-01", "5.8210e+00"],
            ["9.6490e-01", "5.9319e+00"],
            ["9.8063e-01", "6.0440e+00"],
            ["9.9662e-01", "6.1573e+00"],
            ["1.0129e+00", "6.2718e+00"],
            ["1.0294e+00", "6.3875e+00"],
            ["1.0462e+00", "6.5046e+00"],
            ["1.0632e+00", "6.6231e+00"],
            ["1.0806e+00", "6.7429e+00"],
            ["1.0982e+00", "6.8642e+00"],
            ["1.1161e+00", "6.9869e+00"],
            ["1.1343e+00", "7.1112e+00"],
            ["1.1528e+00", "7.2370e+00"],
            ["1.1716e+00", "7.3644e+00"],
            ["1.1907e+00", "7.4935e+00"],
            ["1.2101e+00", "7.6242e+00"],
            ["1.2299e+00", "7.7566e+00"],
            ["1.2499e+00", "7.8908e+00"],
            ["1.2703e+00", "8.0268e+00"],
            ["1.2910e+00", "8.1646e+00"],
            ["1.3121e+00", "8.3044e+00"],
            ["1.3335e+00", "8.4460e+00"],
            ["1.3552e+00", "8.5896e+00"],
            ["1.3773e+00", "8.7353e+00"],
            ["1.3998e+00", "8.8829e+00"],
            ["1.4226e+00", "9.0327e+00"],
            ["1.4458e+00", "9.1847e+00"],
            ["1.4694e+00", "9.3388e+00"],
            ["1.4933e+00", "9.4951e+00"],
            ["1.5177e+00", "9.6538e+00"],
            ["1.5424e+00", "9.8147e+00"],
            ["1.5676e+00", "9.9780e+00"],
            ["1.5931e+00", "1.0144e+01"],
            ["1.6191e+00", "1.0312e+01"],
            ["1.6455e+00", "1.0483e+01"],
            ["1.6723e+00", "1.0656e+01"],
            ["1.6996e+00", "1.0832e+01"],
            ["1.7273e+00", "1.1010e+01"],
            ["1.7555e+00", "1.1192e+01"],
            ["1.7841e+00", "1.1376e+01"],
            ["1.8132e+00", "1.1563e+01"],
            ["1.8428e+00", "1.1752e+01"],
            ["1.8728e+00", "1.1945e+01"],
            ["1.9034e+00", "1.2140e+01"],
            ["1.9344e+00", "1.2339e+01"],
            ["1.9660e+00", "1.2541e+01"],
            ["1.9980e+00", "1.2745e+01"],
            ["2.0306e+00", "1.2953e+01"],
            ["2.0637e+00", "1.3164e+01"],
            ["2.0974e+00", "1.3379e+01"],
            ["2.1316e+00", "1.3597e+01"],
            ["2.1663e+00", "1.3818e+01"],
            ["2.2016e+00", "1.4042e+01"],
            ["2.2375e+00", "1.4271e+01"],
            ["2.2740e+00", "1.4502e+01"],
            ["2.3111e+00", "1.4738e+01"],
            ["2.3488e+00", "1.4977e+01"],
            ["2.3871e+00", "1.5219e+01"],
            ["2.4260e+00", "1.5466e+01"],
            ["2.4656e+00", "1.5717e+01"],
            ["2.5058e+00", "1.5971e+01"],
            ["2.5467e+00", "1.6229e+01"],
            ["2.5882e+00", "1.6492e+01"],
            ["2.6304e+00", "1.6758e+01"],
            ["2.6733e+00", "1.7029e+01"],
            ["2.7169e+00", "1.7304e+01"],
            ["2.7612e+00", "1.7584e+01"],
            ["2.8062e+00", "1.7867e+01"],
            ["2.8520e+00", "1.8156e+01"],
            ["2.8985e+00", "1.8448e+01"],
            ["2.9457e+00", "1.8746e+01"],
            ["2.9938e+00", "1.9048e+01"],
            ["3.0426e+00", "1.9354e+01"],
            ["3.0922e+00", "1.9666e+01"],
            ["3.1426e+00", "1.9982e+01"],
            ["3.1939e+00", "2.0304e+01"],
            ["3.2460e+00", "2.0630e+01"],
            ["3.2989e+00", "2.0962e+01"],
            ["3.3527e+00", "2.1299e+01"],
            ["3.4074e+00", "2.1640e+01"],
            ["3.4629e+00", "2.1988e+01"],
            ["3.5194e+00", "2.2340e+01"],
            ["3.5768e+00", "2.2699e+01"],
            ["3.6351e+00", "2.3062e+01"],
            ["3.6944e+00", "2.3432e+01"],
            ["3.7546e+00", "2.3807e+01"],
            ["3.8159e+00", "2.4188e+01"],
            ["3.8781e+00", "2.4575e+01"],
            ["3.9413e+00", "2.4967e+01"],
            ["4.0056e+00", "2.5366e+01"],
            ["4.0709e+00", "2.5771e+01"],
            ["4.1373e+00", "2.6182e+01"],
            ["4.2048e+00", "2.6600e+01"],
            ["4.2733e+00", "2.7023e+01"],
            ["4.3430e+00", "2.7454e+01"],
            ["4.4138e+00", "2.7890e+01"],
            ["4.4858e+00", "2.8334e+01"],
            ["4.5589e+00", "2.8784e+01"],
            ["4.6333e+00", "2.9241e+01"],
            ["4.7088e+00", "2.9705e+01"],
            ["4.7856e+00", "3.0176e+01"],
            ["4.8637e+00", "3.0653e+01"],
            ["4.9430e+00", "3.1139e+01"],
            ["5.0236e+00", "3.1631e+01"],
            ["5.1055e+00", "3.2130e+01"],
            ["5.1888e+00", "3.2637e+01"],
            ["5.2734e+00", "3.3152e+01"],
            ["5.3594e+00", "3.3674e+01"],
            ["5.4468e+00", "3.4204e+01"],
            ["5.5356e+00", "3.4741e+01"],
            ["5.6258e+00", "3.5287e+01"],
            ["5.7176e+00", "3.5840e+01"],
            ["5.8108e+00", "3.6401e+01"],
            ["5.9056e+00", "3.6971e+01"],
            ["6.0019e+00", "3.7548e+01"],
            ["6.0997e+00", "3.8134e+01"],
            ["6.1992e+00", "3.8728e+01"],
        ],
    )
    model.java.component("comp1").material("mat3").propertyGroup(
        "RefractiveIndex"
    ).func("int2").set("fununit", ["1"])
    model.java.component("comp1").material("mat3").propertyGroup(
        "RefractiveIndex"
    ).func("int2").set("argunit", ["um"])
    model.java.component("comp1").material("mat3").propertyGroup("RefractiveIndex").set(
        "n",
        [
            "nr(c_const/freq)",
            "0",
            "0",
            "0",
            "nr(c_const/freq)",
            "0",
            "0",
            "0",
            "nr(c_const/freq)",
        ],
    )
    model.java.component("comp1").material("mat3").propertyGroup("RefractiveIndex").set(
        "ki",
        [
            "ni(c_const/freq)",
            "0",
            "0",
            "0",
            "ni(c_const/freq)",
            "0",
            "0",
            "0",
            "ni(c_const/freq)",
        ],
    )
    model.java.component("comp1").material("mat3").propertyGroup(
        "RefractiveIndex"
    ).addInput("frequency")

    model.java.component("comp1").cpl("intop1").set("opname", "intop_vol")
    model.java.component("comp1").cpl("intop2").set("opname", "intop_surf")

    model.java.component("comp1").coordSystem("pml1").set("wavelengthSource", "ewfd2")

    model.java.component("comp1").physics("ewfd").feature("wee1").set(
        "DisplacementFieldModel", "RelativePermittivity"
    )
    model.java.component("comp1").physics("ewfd").feature("wee1").set(
        "omegap", "13.8*10^15"
    )
    model.java.component("comp1").physics("ewfd").feature("wee1").set("f", Integer(1))
    model.java.component("comp1").physics("ewfd").feature("wee1").set(
        "omega0", "400[THz]"
    )
    model.java.component("comp1").physics("ewfd").feature("wee1").set(
        "epsilonr_mat", "userdef"
    )
    model.java.component("comp1").physics("ewfd").feature("wee1").set(
        "epsilonr", [[0.054007], [0], [0], [0], [0.054007], [0], [0], [0], [0.054007]]
    )
    model.java.component("comp1").physics("ewfd").feature("wee1").set(
        "epsilonInf_mat", "from_mat"
    )
    model.java.component("comp1").physics("ewfd").feature("wee1").set(
        "mur_mat", "userdef"
    )
    model.java.component("comp1").physics("ewfd").feature("wee1").set(
        "sigma_mat", "userdef"
    )
    model.java.component("comp1").physics("ewfd").feature("wee1").set(
        "sigma",
        [["45e6"], ["0"], ["0"], ["0"], ["45e6"], ["0"], ["0"], ["0"], ["45e6"]],
    )
    model.java.component("comp1").physics("ewfd").feature("wee2").set(
        "n", [["na"], ["0"], ["0"], ["0"], ["na"], ["0"], ["0"], ["0"], ["na"]]
    )
    model.java.component("comp1").physics("ewfd").feature("port1").set("Pin", "P")
    model.java.component("comp1").physics("ewfd").feature("port1").set(
        "PortType", "Periodic"
    )
    model.java.component("comp1").physics("ewfd").feature("port1").set(
        "Eampl", [["E0x"], ["E0y"], ["0"]]
    )
    model.java.component("comp1").physics("ewfd").feature("port1").set(
        "alpha1_inc", "theta"
    )
    model.java.component("comp1").physics("ewfd").feature("port1").set(
        "alpha2_inc", "phi"
    )
    model.java.component("comp1").physics("ewfd").feature("port1").set(
        "n", [["na"], ["0"], ["0"], ["0"], ["na"], ["0"], ["0"], ["0"], ["na"]]
    )
    model.java.component("comp1").physics("ewfd").feature("port2").set(
        "PortType", "Periodic"
    )
    model.java.component("comp1").physics("ewfd").feature("port2").set(
        "Eampl", [["E0x"], ["E0y"], ["0"]]
    )
    model.java.component("comp1").physics("ewfd").feature("port2").set(
        "n", [["nb"], ["0"], ["0"], ["0"], ["nb"], ["0"], ["0"], ["0"], ["nb"]]
    )
    model.java.component("comp1").physics("ewfd").feature("pc1").set(
        "PeriodicType", "Floquet"
    )
    model.java.component("comp1").physics("ewfd").feature("pc1").set(
        "Floquet_source", "FromPeriodicPort"
    )
    model.java.component("comp1").physics("ewfd").feature("pc2").set(
        "PeriodicType", "Floquet"
    )
    model.java.component("comp1").physics("ewfd").feature("pc2").set(
        "Floquet_source", "FromPeriodicPort"
    )
    model.java.component("comp1").physics("ewfd2").prop("BackgroundField").set(
        "SolveFor", "scatteredField"
    )
    model.java.component("comp1").physics("ewfd2").prop("BackgroundField").set(
        "Eb", [["ewfd.Ex"], ["ewfd.Ey"], ["ewfd.Ez"]]
    )
    model.java.component("comp1").physics("ewfd2").feature("wee1").set(
        "DisplacementFieldModel", "RelativePermittivity"
    )
    model.java.component("comp1").physics("ewfd2").feature("wee1").set(
        "omegap", "13.8*10^15"
    )
    model.java.component("comp1").physics("ewfd2").feature("wee1").set("f", Integer(1))
    model.java.component("comp1").physics("ewfd2").feature("wee1").set(
        "omega0", "400[THz]"
    )
    model.java.component("comp1").physics("ewfd2").feature("wee1").set(
        "mur_mat", "userdef"
    )
    model.java.component("comp1").physics("ewfd2").feature("wee1").set(
        "sigma_mat", "userdef"
    )

    model.java.component("comp1").mesh("mesh1").feature("size").set("custom", "on")
    model.java.component("comp1").mesh("mesh1").feature("size").set("hmax", "lda0/6")
    model.java.component("comp1").mesh("mesh1").feature("size2").set("custom", "on")
    model.java.component("comp1").mesh("mesh1").feature("size2").set(
        "hmax", "lda0/6/nb"
    )
    model.java.component("comp1").mesh("mesh1").feature("size2").set(
        "hmaxactive", JBoolean(True)
    )

    model.java.component("comp1").mesh("mesh1").feature("ftet1").selection().named(
        "geom1_mov2_dom"
    )  # select Nanoparticle
    model.java.component("comp1").mesh("mesh1").feature("ftet1").selection().add(
        18, 19
    )  # select air and substrate domain

    model.java.component("comp1").mesh("mesh1").feature("swe1").feature("dis1").set(
        "numelem", Integer(8)
    )
    model.java.component("comp1").mesh("mesh1").run()

    model.java.study().create("std1")
    model.java.study("std1").create("wave", "Wavelength")
    model.java.study("std1").create("wave2", "Wavelength")
    model.java.study("std1").feature("wave").set(
        "activate",
        ["ewfd", "on", "ewfd2", "off", "frame:spatial1", "on", "frame:material1", "on"],
    )
    model.java.study("std1").feature("wave2").set(
        "activate",
        ["ewfd", "off", "ewfd2", "on", "frame:spatial1", "on", "frame:material1", "on"],
    )

    model.java.sol().create("sol1")
    model.java.sol("sol1").study("std1")
    model.java.sol("sol1").attach("std1")
    model.java.sol("sol1").create("st1", "StudyStep")
    model.java.sol("sol1").create("v1", "Variables")
    model.java.sol("sol1").create("s1", "Stationary")
    model.java.sol("sol1").create("st2", "StudyStep")
    model.java.sol("sol1").create("v2", "Variables")
    model.java.sol("sol1").create("s2", "Stationary")
    model.java.sol("sol1").feature("s1").create("p1", "Parametric")
    model.java.sol("sol1").feature("s1").create("fc1", "FullyCoupled")
    model.java.sol("sol1").feature("s1").create("d1", "Direct")
    model.java.sol("sol1").feature("s1").create("i1", "Iterative")
    model.java.sol("sol1").feature("s1").feature("i1").create("mg1", "Multigrid")
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "pr"
    ).create("va1", "Vanka")
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "po"
    ).create("sv1", "SORVector")
    model.java.sol("sol1").feature("s1").feature().remove("fcDef")
    model.java.sol("sol1").feature("s2").create("p1", "Parametric")
    model.java.sol("sol1").feature("s2").create("fc1", "FullyCoupled")
    model.java.sol("sol1").feature("s2").create("i1", "Iterative")
    model.java.sol("sol1").feature("s2").create("i2", "Iterative")
    model.java.sol("sol1").feature("s2").feature("i1").create("mg1", "Multigrid")
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").feature(
        "pr"
    ).create("sv1", "SORVector")
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").feature(
        "po"
    ).create("sv1", "SORVector")
    model.java.sol("sol1").feature("s2").feature("i2").create("mg1", "Multigrid")
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").feature(
        "pr"
    ).create("sv1", "SORVector")
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").feature(
        "po"
    ).create("sv1", "SORVector")
    model.java.sol("sol1").feature("s2").feature().remove("fcDef")

    model.java.result().dataset("dset1").selection().named("geom1_mov2_dom")
    model.java.result().numerical().create("int1", "IntVolume")
    model.java.result().numerical("int1").selection().named("geom1_mov2_dom")
    model.java.result().numerical("int1").set("probetag", "none")
    model.java.result().create("pg1", "PlotGroup3D")
    model.java.result("pg1").create("surf1", "Surface")
    model.java.result("pg1").feature("surf1").set("expr", "ewfd2.Qh")

    model.java.study("std1").feature("wave").set("plist", "lda0")
    model.java.study("std1").feature("wave2").set("plist", "lda0")

    model.java.sol("sol1").attach("std1")
    model.java.sol("sol1").feature("st1").label("Compile Equations: Wavelength Domain")
    model.java.sol("sol1").feature("v1").label("Dependent Variables 1.1")
    model.java.sol("sol1").feature("v1").set("clistctrl", ["p1"])
    model.java.sol("sol1").feature("v1").set("cname", ["lambda0"])
    model.java.sol("sol1").feature("v1").set("clist", ["lda0"])
    model.java.sol("sol1").feature("s1").label("Stationary Solver 1.1")
    model.java.sol("sol1").feature("s1").set("stol", 0.01)
    model.java.sol("sol1").feature("s1").feature("dDef").label("Direct 2")
    model.java.sol("sol1").feature("s1").feature("aDef").label("Advanced 1")
    model.java.sol("sol1").feature("s1").feature("aDef").set(
        "complexfun", JBoolean(True)
    )
    model.java.sol("sol1").feature("s1").feature("p1").label("Parametric 1.1")
    model.java.sol("sol1").feature("s1").feature("p1").set("pname", ["lambda0"])
    model.java.sol("sol1").feature("s1").feature("p1").set("plistarr", ["lda0"])
    model.java.sol("sol1").feature("s1").feature("p1").set("punit", ["\u00b5m"])
    model.java.sol("sol1").feature("s1").feature("p1").set("pcontinuationmode", "no")
    model.java.sol("sol1").feature("s1").feature("p1").set("preusesol", "auto")
    model.java.sol("sol1").feature("s1").feature("fc1").label("Fully Coupled 1.1")
    model.java.sol("sol1").feature("s1").feature("fc1").set("linsolver", "d1")
    model.java.sol("sol1").feature("s1").feature("d1").label(
        "Suggested Direct Solver (ewfd)"
    )
    model.java.sol("sol1").feature("s1").feature("i1").label(
        "Suggested Iterative Solver (ewfd)"
    )
    model.java.sol("sol1").feature("s1").feature("i1").set("itrestart", Integer(300))
    model.java.sol("sol1").feature("s1").feature("i1").set("prefuntype", "right")
    model.java.sol("sol1").feature("s1").feature("i1").feature("ilDef").label(
        "Incomplete LU 1"
    )
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").label(
        "Multigrid 1.1"
    )
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").set(
        "iter", Integer(1)
    )
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "pr"
    ).label("Presmoother 1")
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "pr"
    ).feature("soDef").label("SOR 1")
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "pr"
    ).feature("va1").label("Vanka 1.1")
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "pr"
    ).feature("va1").set("iter", Integer(1))
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "pr"
    ).feature("va1").set("vankavars", ["comp1_E"])
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "pr"
    ).feature("va1").set("vankasolv", "stored")
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "pr"
    ).feature("va1").set("vankarelax", 0.95)
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "po"
    ).label("Postsmoother 1")
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "po"
    ).feature("soDef").label("SOR 1")
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "po"
    ).feature("sv1").label("SOR Vector 1.1")
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "po"
    ).feature("sv1").set("iter", Integer(1))
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "po"
    ).feature("sv1").set("relax", 0.5)
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "po"
    ).feature("sv1").set("sorvecdof", ["comp1_E"])
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "cs"
    ).label("Coarse Solver 1")
    model.java.sol("sol1").feature("s1").feature("i1").feature("mg1").feature(
        "cs"
    ).feature("dDef").label("Direct 1")
    model.java.sol("sol1").feature("st2").label(
        "Compile Equations: Wavelength Domain 2"
    )
    model.java.sol("sol1").feature("st2").set("studystep", "wave2")
    model.java.sol("sol1").feature("v2").label("Dependent Variables 2.1")
    model.java.sol("sol1").feature("v2").set("initmethod", "sol")
    model.java.sol("sol1").feature("v2").set("initsol", "sol1")
    model.java.sol("sol1").feature("v2").set("solnum", "auto")
    model.java.sol("sol1").feature("v2").set("notsolmethod", "sol")
    model.java.sol("sol1").feature("v2").set("notsol", "sol1")
    model.java.sol("sol1").feature("v2").set("notsolnum", "auto")
    model.java.sol("sol1").feature("v2").set("clistctrl", ["p1"])
    model.java.sol("sol1").feature("v2").set("cname", ["lambda0"])
    model.java.sol("sol1").feature("v2").set("clist", ["lda0"])
    model.java.sol("sol1").feature("s2").label("Stationary Solver 2.1")
    model.java.sol("sol1").feature("s2").feature("dDef").label("Direct 1")
    model.java.sol("sol1").feature("s2").feature("aDef").label("Advanced 1")
    model.java.sol("sol1").feature("s2").feature("aDef").set(
        "complexfun", JBoolean(True)
    )
    model.java.sol("sol1").feature("s2").feature("p1").label("Parametric 1.1")
    model.java.sol("sol1").feature("s2").feature("p1").set("pname", ["lambda0"])
    model.java.sol("sol1").feature("s2").feature("p1").set("plistarr", ["lda0"])
    model.java.sol("sol1").feature("s2").feature("p1").set("punit", ["\u00b5m"])
    model.java.sol("sol1").feature("s2").feature("p1").set("pcontinuationmode", "no")
    model.java.sol("sol1").feature("s2").feature("p1").set("preusesol", "auto")
    model.java.sol("sol1").feature("s2").feature("fc1").label("Fully Coupled 1.1")
    model.java.sol("sol1").feature("s2").feature("fc1").set("linsolver", "i1")
    model.java.sol("sol1").feature("s2").feature("i1").label(
        "Suggested Iterative Solver (ewfd2)"
    )
    model.java.sol("sol1").feature("s2").feature("i1").set("linsolver", "bicgstab")
    model.java.sol("sol1").feature("s2").feature("i1").feature("ilDef").label(
        "Incomplete LU 1"
    )
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").label(
        "Multigrid 1.1"
    )
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").feature(
        "pr"
    ).label("Presmoother 1")
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").feature(
        "pr"
    ).feature("soDef").label("SOR 1")
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").feature(
        "pr"
    ).feature("sv1").label("SOR Vector 1.1")
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").feature(
        "pr"
    ).feature("sv1").set("sorvecdof", ["comp1_E2"])
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").feature(
        "po"
    ).label("Postsmoother 1")
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").feature(
        "po"
    ).feature("soDef").label("SOR 1")
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").feature(
        "po"
    ).feature("sv1").label("SOR Vector 1.1")
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").feature(
        "po"
    ).feature("sv1").set("sorvecdof", ["comp1_E2"])
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").feature(
        "cs"
    ).label("Coarse Solver 1")
    model.java.sol("sol1").feature("s2").feature("i1").feature("mg1").feature(
        "cs"
    ).feature("dDef").label("Direct 1")
    model.java.sol("sol1").feature("s2").feature("i2").label(
        "Suggested Iterative Solver (ewfd2) 2"
    )
    model.java.sol("sol1").feature("s2").feature("i2").set("linsolver", "fgmres")
    model.java.sol("sol1").feature("s2").feature("i2").feature("ilDef").label(
        "Incomplete LU 1"
    )
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").label(
        "Multigrid 1.1"
    )
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").feature(
        "pr"
    ).label("Presmoother 1")
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").feature(
        "pr"
    ).feature("soDef").label("SOR 1")
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").feature(
        "pr"
    ).feature("sv1").label("SOR Vector 1.1")
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").feature(
        "pr"
    ).feature("sv1").set("sorvecdof", ["comp1_E2"])
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").feature(
        "po"
    ).label("Postsmoother 1")
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").feature(
        "po"
    ).feature("soDef").label("SOR 1")
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").feature(
        "po"
    ).feature("sv1").label("SOR Vector 1.1")
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").feature(
        "po"
    ).feature("sv1").set("sorvecdof", ["comp1_E2"])
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").feature(
        "cs"
    ).label("Coarse Solver 1")
    model.java.sol("sol1").feature("s2").feature("i2").feature("mg1").feature(
        "cs"
    ).feature("dDef").label("Direct 1")
    model.java.sol("sol1").runAll()

    model.java.result().numerical("int1").label("LightToHeat")
    model.java.result().numerical("int1").set("table", "tbl13")
    model.java.result().numerical("int1").set("expr", ["ewfd2.Qh/(I0*w*w)"])
    model.java.result().numerical("int1").set("unit", ["1"])
    model.java.result().numerical("int1").set("descr", [""])
    model.java.result().numerical("int1").setResult()
    model.java.result("pg1").feature("surf1").set("resolution", "normal")

    model.java.study("std1").run()

    print(model.java.result().numerical("int1").computeResult()[0][0][0])
    elapsedTime = time.process_time() - startTime

    print(f'Simulation ran for {elapsedTime}s')

    return model.java.result().numerical("int1").computeResult()[0][0][0]
