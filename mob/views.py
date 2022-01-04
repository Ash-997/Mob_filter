from django.shortcuts import render
from .models import Brand, Mobiles, Ram, Memory, Pricecat


def show(request):
    brands = Brand.objects.all()
    rams = Ram.objects.all()
    memory = Memory.objects.all()
    pcats = Pricecat.objects.all()
    context = {'brands': brands, "rams": rams, "memos": memory, 'pcats': pcats}
    return render(request, 'doom.html', context)


def gta(request):
    print("start----------------++++++++++++++++")

    global context

    context = {}
    context.clear()
    # print(request.get_full_path)
    # if str(request) == "WSGIRequest: GET '/goom'?":
    #     return render(request, 'vf.html', context)


    products = []
    fil_prod = []
    final = []
    wefinal = []
    allfil = []
    rams = []
    products.clear()
    fil_prod.clear()
    final.clear()
    wefinal.clear()
    allfil.clear()
    rams.clear()

    rams.extend(Ram.objects.all())

    appul = request.GET.get('Apple')
    sam = request.GET.get('Samsung')
    Nok = request.GET.get('Nokia')
    mi = request.GET.get('MI')
    red = request.GET.get('Realme')

    chargb = request.GET.get('4GB')
    aathggb = request.GET.get('8GB')
    baragb = request.GET.get('12GB')

    btgb = request.GET.get('32GB')
    csgb = request.GET.get('64GB')
    ekathgb = request.GET.get('128GB')

    upto10 = request.GET.get('0 - 10K')
    upto20 = request.GET.get('10K - 20K')
    upto30 = request.GET.get('20k-30k')
    upto40 = request.GET.get('30k - 40k')
    upto50 = request.GET.get('40k - 50k')
    above50 = request.GET.get('50k and above')

    if appul:
        # nik = Mobiles.objects.filter(brnd_id=appul)
        products.extend(Mobiles.objects.filter(brnd_id=appul))
        # print(products)
        context = {"pros": products}

    # return render(request,'vf.html',context)
    if sam:
        products.extend(Mobiles.objects.filter(brnd_id=sam))
        context = {"pros": products}
        # print(products)
    if Nok:
        products.extend(Mobiles.objects.filter(brnd_id=Nok))
        context = {"pros": products}
        # print(products)
    if mi:
        products.extend(Mobiles.objects.filter(brnd_id=mi))
        context = {"pros": products}
        # print(products)
    if red:
        products.extend(Mobiles.objects.filter(brnd_id=red))
        context = {"pros": products}

    if chargb:
        if products:
            for product in products:
                if str(product.ram_id) == chargb:
                    fil_prod.append(product)

            context = {"pros": fil_prod}
        else:
            fil_prod.extend(Mobiles.objects.filter(ram_id=chargb))
            context = {"pros": fil_prod}

    if aathggb:
        if products:
            for product in products:
                if str(product.ram_id) == aathggb:
                    fil_prod.append(product)
            context = {"pros": fil_prod}
        else:
            fil_prod.extend(Mobiles.objects.filter(ram_id=aathggb))
            context = {"pros": fil_prod}
    if baragb:
        if products:
            for product in products:
                if str(product.ram_id) == baragb:
                    fil_prod.append(product)

            context = {"pros": fil_prod}
        else:
            fil_prod.extend(Mobiles.objects.filter(ram_id=baragb))
            context = {"pros": fil_prod}

    if btgb:

        if fil_prod:
            for product in fil_prod:
                if str(product.memory_id) == btgb:
                    final.append(product)

            context = {"pros": final}
        elif chargb or aathggb or baragb:

            if not fil_prod:
                context = {"pros": final}

        elif products:
            for product in products:
                if str(product.memory_id) == btgb:
                    final.append(product)
            context = {"pros": final}

        else:
            wefinal.extend(Mobiles.objects.filter(memory_id=btgb))
            context = {"pros": wefinal}

    if csgb:

        if fil_prod:
            for product in fil_prod:
                if str(product.memory_id) == csgb:
                    final.append(product)

            context = {"pros": final}
        elif chargb or aathggb or baragb:
            if not fil_prod:
                context = {"pros": final}

        elif products:
            for product in products:
                if str(product.memory_id) == csgb:
                    final.append(product)
            context = {"pros": final}

        else:
            wefinal.extend(Mobiles.objects.filter(memory_id=csgb))
            context = {"pros": wefinal}

    if ekathgb:

        if fil_prod:
            for product in fil_prod:
                if str(product.memory_id) == ekathgb:
                    final.append(product)

            context = {"pros": final}
        elif chargb or aathggb or baragb:
            if not fil_prod:
                context = {"pros": final}

        elif products:
            for product in products:
                if str(product.memory_id) == ekathgb:
                    final.append(product)
            context = {"pros": final}

        else:
            wefinal.extend(Mobiles.objects.filter(memory_id=ekathgb))
            context = {"pros": wefinal}

    if upto10:
        print("upto 10 working")
        if btgb or csgb or ekathgb:
            if appul or Nok or sam or mi or red:
                if chargb or aathggb or baragb:

                    if final:
                        for product in final:
                            if str(product.pricecat_id) == upto10:
                                allfil.append(product)
                        context = {"pros": allfil}
                        #return render(request, 'vf.html', context)
                    else:
                        #return render(request, 'vf.html', context)
                        pass

        if wefinal:
            for product in wefinal:
                if str(product.pricecat_id) == upto10:
                    allfil.append(product)
            context = {"pros": allfil}

        elif fil_prod:
         if not allfil:

            if btgb or csgb or ekathgb:
                for product in fil_prod:
                    if str(product.memory_id) == btgb:
                        if str(product.pricecat_id) == upto10:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == csgb:
                        if str(product.pricecat_id) == upto10:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == ekathgb:
                        if str(product.pricecat_id) == upto10:
                            allfil.append(product)
                        context = {"pros": allfil}
                #return render(request, 'vf.html', context)
            else:
             for product in fil_prod:
                if str(product.pricecat_id) == upto10:
                    allfil.append(product)
             context = {"pros": allfil}


        elif chargb or aathggb or baragb:
            print("kabab me haaddi")
            if not fil_prod:
                context = {"pros": final}

        elif products:
            if btgb or csgb or ekathgb:
                for product in products:
                    if str(product.memory_id) == btgb:
                        if str(product.pricecat_id) == upto10:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == csgb:
                        if str(product.pricecat_id) == upto10:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == ekathgb:
                        if str(product.pricecat_id) == upto10:
                            allfil.append(product)
                    context = {"pros": allfil}
                print(allfil)
                #return render(request, 'vf.html', context)
            else:
             for product in products:
                if str(product.pricecat_id) == upto10:
                    allfil.append(product)
             context = {"pros": allfil}
            # if chargb or aathggb or baragb or btgb or csgb or ekathgb:
            #     print("ghghghghghgh")
            #     if not final:
            #         context = {"pros": final}

        else:
            allfil.extend(Mobiles.objects.filter(pricecat=upto10))
            context = {"pros": allfil}

    if upto20:
        print("upto 20 working")
        if btgb or csgb or ekathgb:
            if appul or Nok or sam or mi or red:
                if chargb or aathggb or baragb:

                    if final:
                        for product in final:
                            if str(product.pricecat_id) == upto20:
                                allfil.append(product)
                        context = {"pros": allfil}
                        #return render(request, 'vf.html', context)
                    else:
                        #return render(request, 'vf.html', context)
                        pass

        if wefinal:
            print("bgbgbgbgbgbgbgbg")
            for product in wefinal:
                if str(product.pricecat_id) == upto20:
                    allfil.append(product)
            context = {"pros": allfil}

        elif fil_prod:
          if not allfil:

            if btgb or csgb or ekathgb:
                for product in fil_prod:
                    if str(product.memory_id) == btgb:
                        if str(product.pricecat_id) == upto20:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == csgb:
                        if str(product.pricecat_id) == upto20:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == ekathgb:
                        if str(product.pricecat_id) == upto20:
                            allfil.append(product)
                        context = {"pros": allfil}
               # return render(request, 'vf.html', context)
            else:
             for product in fil_prod:
                if str(product.pricecat_id) == upto20:
                    allfil.append(product)
             context = {"pros": allfil}


        elif chargb or aathggb or baragb:
            print("kabab me haaddi")
            if not fil_prod:
                context = {"pros": final}

        elif products:
            if btgb or csgb or ekathgb:
                for product in products:
                    if str(product.memory_id) == btgb:
                        if str(product.pricecat_id) == upto20:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == csgb:
                        if str(product.pricecat_id) == upto20:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == ekathgb:
                        if str(product.pricecat_id) == upto20:
                            allfil.append(product)
                    context = {"pros": allfil}
                print(allfil)
                #return render(request, 'vf.html', context)

            else:
             for product in products:
                if str(product.pricecat_id) == upto20:
                    allfil.append(product)
             context = {"pros": allfil}
            # if chargb or aathggb or baragb or btgb or csgb or ekathgb:
            #     print("ghghghghghgh")
            #     if not final:
            #         context = {"pros": final}
            print(allfil)
        else:
            allfil.extend(Mobiles.objects.filter(pricecat=upto20))
            context = {"pros": allfil}

    if upto30:
        print("upto 30 working")
        if btgb or csgb or ekathgb:
            if appul or Nok or sam or mi or red:
                if chargb or aathggb or baragb:

                    if final:
                        for product in final:
                            if str(product.pricecat_id) == upto30:
                                allfil.append(product)
                        context = {"pros": allfil}
                        #return render(request, 'vf.html', context)
                    else:
                        #return render(request, 'vf.html', context)
                        pass

        if wefinal:
            for product in wefinal:
                if str(product.pricecat_id) == upto30:
                    allfil.append(product)
            context = {"pros": allfil}

        elif fil_prod:
         if not allfil:
            if btgb or csgb or ekathgb:
                for product in fil_prod:
                    if str(product.memory_id) == btgb:
                        if str(product.pricecat_id) == upto30:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == csgb:
                        if str(product.pricecat_id) == upto30:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == ekathgb:
                        if str(product.pricecat_id) == upto30:
                            allfil.append(product)
                        context = {"pros": allfil}
                #return render(request, 'vf.html', context)
            else:
             for product in fil_prod:
                if str(product.pricecat_id) == upto30:
                    allfil.append(product)
             context = {"pros": allfil}


        elif chargb or aathggb or baragb:
            if not fil_prod:
                context = {"pros": final}

        elif products:
            if btgb or csgb or ekathgb:
                for product in products:
                    if str(product.memory_id) == btgb:
                        if str(product.pricecat_id) == upto30:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == csgb:
                        if str(product.pricecat_id) == upto30:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == ekathgb:
                        if str(product.pricecat_id) == upto30:
                            allfil.append(product)
                    context = {"pros": allfil}
                #return render(request, 'vf.html', context)
            else:
             for product in products:
                if str(product.pricecat_id) == upto30:
                    allfil.append(product)
             context = {"pros": allfil}
            # if chargb or aathggb or baragb or btgb or csgb or ekathgb:
            #     print("ghghghghghgh")
            #     if not final:
            #         context = {"pros": final}
            print(allfil)
        else:
            allfil.extend(Mobiles.objects.filter(pricecat=upto30))
            context = {"pros": allfil}

    if upto40:

        print("upto 40 working")
        if btgb or csgb or ekathgb:
            if appul or Nok or sam or mi or red:
                if chargb or aathggb or baragb:

                    if final:
                        for product in final:
                            if str(product.pricecat_id) == upto40:
                                allfil.append(product)
                        context = {"pros": allfil}
                        #return render(request, 'vf.html', context)
                    else:
                        #return render(request, 'vf.html', context)
                        pass

        if wefinal:
            print("bgbgbgbgbgbgbgbg")
            for product in wefinal:
                if str(product.pricecat_id) == upto40:
                    allfil.append(product)
            context = {"pros": allfil}

        elif fil_prod:
          if not allfil:

            if btgb or csgb or ekathgb:
                for product in fil_prod:
                    if str(product.memory_id) == btgb:
                        if str(product.pricecat_id) == upto40:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == csgb:
                        if str(product.pricecat_id) == upto40:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == ekathgb:
                        if str(product.pricecat_id) == upto40:
                            allfil.append(product)
                        context = {"pros": allfil}
                #return render(request, 'vf.html', context)

            else:
             for product in fil_prod:
                if str(product.pricecat_id) == upto40:
                    allfil.append(product)
             context = {"pros": allfil}


        elif chargb or aathggb or baragb:
            if not fil_prod:
                context = {"pros": final}

        elif products:
            if btgb or csgb or ekathgb:
                for product in products:
                    if str(product.memory_id) == btgb:
                        if str(product.pricecat_id) == upto40:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == csgb:
                        if str(product.pricecat_id) == upto40:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == ekathgb:
                        if str(product.pricecat_id) == upto40:
                            allfil.append(product)
                    context = {"pros": allfil}
                #return render(request, 'vf.html', context)
            else:
             for product in products:
                if str(product.pricecat_id) == upto40:
                    allfil.append(product)
             context = {"pros": allfil}
            # if chargb or aathggb or baragb or btgb or csgb or ekathgb:
            #     print("ghghghghghgh")
            #     if not final:
            #         context = {"pros": final}
            print(allfil)
        else:
            allfil.extend(Mobiles.objects.filter(pricecat=upto40))
            context = {"pros": allfil}

    if upto50:
        if btgb or csgb or ekathgb:
            if appul or Nok or sam or mi or red:
                if chargb or aathggb or baragb:

                    if final:
                        for product in final:
                            if str(product.pricecat_id) == upto50:
                                allfil.append(product)
                        context = {"pros": allfil}

                    else:

                        pass

        if wefinal:
            for product in wefinal:
                if str(product.pricecat_id) == upto50:
                    allfil.append(product)
            context = {"pros": allfil}

        elif fil_prod:
          if not allfil:
            if btgb or csgb or ekathgb:
                for product in fil_prod:
                    if str(product.memory_id) == btgb:
                        if str(product.pricecat_id) == upto50:
                         allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == csgb:
                        if str(product.pricecat_id) == upto50:
                         allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == ekathgb:
                        if str(product.pricecat_id) == upto50:
                            allfil.append(product)
                        context = {"pros": allfil}
               # return render(request, 'vf.html', context)
            else:
             for product in fil_prod:
                if str(product.pricecat_id) == upto50:
                    allfil.append(product)
             context = {"pros": allfil}


        elif chargb or aathggb or baragb:
            if not fil_prod:
                context = {"pros": final}

        elif products:
            if btgb or csgb or ekathgb:
                for product in products:
                    if str(product.memory_id) == btgb:
                        if str(product.pricecat_id) == upto50:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == csgb:
                        if str(product.pricecat_id) == upto50:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == ekathgb:
                        if str(product.pricecat_id) == upto50:
                            allfil.append(product)
                    context = {"pros": allfil}
                print(allfil)
               # return render(request, 'vf.html', context)
            else:
             for product in products:
                if str(product.pricecat_id) == upto50:
                    allfil.append(product)
             context = {"pros": allfil}
        # if chargb or aathggb or baragb or btgb or csgb or ekathgb:
        #     print("ghghghghghgh")
        #     if not final:
        #         context = {"pros": final}
            print(allfil)
        else:
            allfil.extend(Mobiles.objects.filter(pricecat=upto50))
            context = {"pros": allfil}

    if above50:

        if btgb or csgb or ekathgb:
            if appul or Nok or sam or mi or red:
                if chargb or aathggb or baragb:

                    if final:
                        for product in final:
                            if str(product.pricecat_id) == above50:
                                allfil.append(product)
                        context = {"pros": allfil}
                    else:
                        pass

        if wefinal:
            for product in wefinal:
                if str(product.pricecat_id) == above50:
                    allfil.append(product)
            context = {"pros": allfil}

        elif fil_prod:
          if not allfil:

            if btgb or csgb or ekathgb:
                for product in fil_prod:
                    if str(product.memory_id) == btgb:
                        if str(product.pricecat_id) == above50:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == csgb:
                        if str(product.pricecat_id) == above50:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == ekathgb:
                        if str(product.pricecat_id) == above50:
                            allfil.append(product)
                        context = {"pros": allfil}
            else:
             for product in fil_prod:
                if str(product.pricecat_id) == above50:
                    allfil.append(product)
             context = {"pros": allfil}


        elif chargb or aathggb or baragb:
            if not fil_prod:
                context = {"pros": final}

        elif products:
            if btgb or csgb or ekathgb:
                for product in products:
                    if str(product.memory_id) == btgb:
                        if str(product.pricecat_id) == above50:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == csgb:
                        if str(product.pricecat_id) == above50:
                            allfil.append(product)
                    context = {"pros": allfil}
                    if str(product.memory_id) == ekathgb:
                        if str(product.pricecat_id) == above50:
                            allfil.append(product)
                    context = {"pros": allfil}

            else:
             for product in products:
                print(products)
                if str(product.pricecat_id) == above50:
                    allfil.append(product)
             context = {"pros": allfil}
            print(allfil)
        else:
            allfil.extend(Mobiles.objects.filter(pricecat=above50))
            context = {"pros": allfil}
    print(context)
    return render(request, 'vf.html', context)









#OLD CODE
        # if final:
        #     print("4rd one")
        #     for product in final:
        #         if str(product.pricecat_id) == upto40:
        #             allfil.append(product)
        #     context = {"pros": allfil}
        #
        #
        #
        #
        # elif fil_prod:
        #     print("dddddd")
        #     for product in fil_prod:
        #         if str(product.pricecat_id) == upto40:
        #             allfil.append(product)
        #     context = {"pros": allfil}
        #
        #
        # elif chargb or aathggb or baragb:
        #     if not fil_prod:
        #         context = {"pros": final}
        #
        # elif products:
        #     for product in products:
        #         if str(product.pricecat_id) == upto40:
        #             allfil.append(product)
        #     context = {"pros": allfil}
        #
        # if chargb or aathggb or baragb or btgb or csgb or ekathgb:
        #     print("787878787878787")
        #     if not final:
        #         context = {"pros": final}
        #
        # else:
        #     allfil.extend(Mobiles.objects.filter(pricecat=upto40))
        #     context = {"pros": allfil}


# if chargb or aathggb or baragb or btgb or csgb or ekathgb:
#     print("ghghghghghgh")
#     if not final:
#         context = {"pros": final}