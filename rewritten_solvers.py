from dsl import *
from constants import *

def solve_67a3c6ac(I):
    return vmirror(I)


def solve_68b16354(I):
    return hmirror(I)


def solve_74dd1130(I):
    return dmirror(I)


def solve_3c9b0459(I):
    return rot180(I)


def solve_6150a2bd(I):
    return rot180(I)


def solve_9172f3a0(I):
    return upscale(I, THREE)


def solve_9dfd6313(I):
    return dmirror(I)


def solve_a416b8f3(I):
    return hconcat(I, I)


def solve_b1948b0a(I):
    return replace(I, SIX, TWO)


def solve_c59eb873(I):
    return upscale(I, TWO)


def solve_c8f0f002(I):
    return replace(I, SEVEN, FIVE)


def solve_d10ecb37(I):
    return crop(I, ORIGIN, TWO_BY_TWO)


def solve_d511f180(I):
    return switch(I, FIVE, EIGHT)


def solve_ed36ccf7(I):
    return rot270(I)


def solve_4c4377d9(I):
    return vconcat(hmirror(I), I)


def solve_6d0aefbc(I):
    return hconcat(I, vmirror(I))


def solve_6fa7a44f(I):
    return vconcat(I, hmirror(I))


def solve_5614dbcf(I):
    return downscale(replace(I, FIVE, ZERO), THREE)


def solve_5bd6f4ac(I):
    return crop(I, tojvec(SIX), THREE_BY_THREE)


def solve_5582e5ca(I):
    return canvas(mostcolor(I), THREE_BY_THREE)


def solve_8be77c9e(I):
    return vconcat(I, hmirror(I))


def solve_c9e6f938(I):
    return hconcat(I, vmirror(I))


def solve_2dee498d(I):
    return first(hsplit(I, THREE))


def solve_1cf80156(I):
    return subgrid(first(objects(I, T, T, T)), I)


def solve_32597951(I):
    return fill(I, THREE, delta(ofcolor(I, EIGHT)))


def solve_25ff71a9(I):
    return move(I, first(objects(I, T, T, T)), DOWN)


def solve_0b148d64(I):
    return subgrid(argmin(partition(I), size), I)


def solve_1f85a75f(I):
    return subgrid(argmax(objects(I, T, T, T), size), I)


def solve_23b5c85d(I):
    return subgrid(argmin(objects(I, T, T, T), size), I)


def solve_9ecd008a(I):
    return subgrid(ofcolor(I, ZERO), vmirror(I))


def solve_ac0a08a4(I):
    return upscale(I, subtract(NINE, colorcount(I, ZERO)))


def solve_be94b721(I):
    return subgrid(argmax(objects(I, T, F, T), size), I)


def solve_c909285e(I):
    return subgrid(ofcolor(I, leastcolor(I)), I)


def solve_f25ffba3(I):
    return vconcat(hmirror(bottomhalf(I)), bottomhalf(I))


def solve_c1d99e64(I):
    return fill(I, TWO, merge(frontiers(I)))


def solve_b91ae062(I):
    return upscale(I, decrement(numcolors(I)))


def solve_3aa6fb7a(I):
    return underfill(I, ONE, mapply(corners, objects(I, T, F, T)))


def solve_7b7f7511(I):
    return apply_func(branch(portrait(I), tophalf, lefthalf), I)


def solve_4258a5f9(I):
    return fill(I, ONE, mapply(neighbors, ofcolor(I, FIVE)))


def solve_2dc579da(I):
    return argmax(mapply(rbind(hsplit, TWO), vsplit(I, TWO)), numcolors)


def solve_28bf18c6(I):
    return hconcat(subgrid(first(objects(I, T, T, T)), I), subgrid(first(
        objects(I, T, T, T)), I))


def solve_3af2c5a8(I):
    return vconcat(hconcat(I, vmirror(I)), hmirror(hconcat(I, vmirror(I))))


def solve_44f52bb0(I):
    return canvas(branch(equality(vmirror(I), I), ONE, SEVEN), UNITY)


def solve_62c24649(I):
    return vconcat(hconcat(I, vmirror(I)), hmirror(hconcat(I, vmirror(I))))


def solve_67e8384a(I):
    return vconcat(hconcat(I, vmirror(I)), hmirror(hconcat(I, vmirror(I))))


def solve_7468f01a(I):
    return vmirror(subgrid(first(objects(I, F, T, T)), I))


def solve_662c240a(I):
    return extract(vsplit(I, THREE), compose(flip, fork(equality, dmirror,
        identity)))


def solve_42a50994(I):
    return cover(I, merge(sizefilter(objects(I, T, T, T), ONE)))


def solve_56ff96f3(I):
    return paint(I, mapply(fork(recolor, color, backdrop), fgpartition(I)))


def solve_50cb2852(I):
    return fill(I, EIGHT, mapply(compose(backdrop, inbox), objects(I, T, F, T))
        )


def solve_4347f46a(I):
    return fill(I, ZERO, mapply(fork(difference, toindices, box), objects(I,
        T, F, T)))


def solve_46f33fce(I):
    return upscale(rot180(downscale(rot180(I), TWO)), FOUR)


def solve_a740d043(I):
    return replace(subgrid(merge(objects(I, T, T, T)), I), ONE, ZERO)


def solve_a79310a0(I):
    return replace(move(I, first(objects(I, T, F, T)), DOWN), EIGHT, TWO)


def solve_aabf363d(I):
    return replace(replace(I, leastcolor(I), ZERO), leastcolor(replace(I,
        leastcolor(I), ZERO)), leastcolor(I))


def solve_ae4f1146(I):
    return subgrid(argmax(objects(I, F, F, T), rbind(colorcount, ONE)), I)


def solve_b27ca6d3(I):
    return fill(I, THREE, mapply(outbox, sizefilter(objects(I, T, F, T), TWO)))


def solve_ce22a75a(I):
    return fill(I, ONE, mapply(backdrop, apply(outbox, objects(I, T, F, T))))


def solve_dc1df850(I):
    return fill(I, ONE, mapply(outbox, colorfilter(objects(I, T, F, T), TWO)))


def solve_f25fbde4(I):
    return upscale(subgrid(first(objects(I, T, T, T)), I), TWO)


def solve_44d8ac46(I):
    return fill(I, TWO, mfilter(apply(delta, objects(I, T, F, T)), square))


def solve_1e0a9b12(I):
    return rot90(apply(rbind(order, identity), rot270(I)))


def solve_0d3d703e(I):
    return switch(switch(switch(switch(I, THREE, FOUR), EIGHT, NINE), TWO,
        SIX), ONE, FIVE)


def solve_3618c87e(I):
    return move(I, merge(sizefilter(objects(I, T, F, T), ONE)), TWO_BY_ZERO)


def solve_1c786137(I):
    return trim(subgrid(argmax(objects(I, T, F, F), height), I))


def solve_8efcae92(I):
    return subgrid(argmax(colorfilter(objects(I, T, F, F), ONE), compose(
        size, delta)), I)


def solve_445eab21(I):
    return canvas(color(argmax(objects(I, T, F, T), fork(multiply, height,
        width))), TWO_BY_TWO)


def solve_6f8cd79b(I):
    return fill(I, EIGHT, mfilter(apply(initset, asindices(I)), rbind(
        bordering, I)))


def solve_2013d3e2(I):
    return tophalf(lefthalf(subgrid(first(objects(I, F, T, T)), I)))


def solve_41e4d17e(I):
    return underfill(I, SIX, mapply(compose(fork(combine, vfrontier,
        hfrontier), center), objects(I, T, F, T)))


def solve_9565186b(I):
    return paint(canvas(FIVE, shape(I)), argmax(objects(I, T, F, F), size))


def solve_aedd82e4(I):
    return fill(I, ONE, merge(sizefilter(colorfilter(objects(I, T, F, F),
        TWO), ONE)))


def solve_bb43febb(I):
    return fill(I, TWO, mapply(compose(backdrop, inbox), colorfilter(
        objects(I, T, F, F), FIVE)))


def solve_e98196ab(I):
    return paint(bottomhalf(I), merge(objects(tophalf(I), T, F, T)))


def solve_f76d97a5(I):
    return replace(switch(I, first(palette(I)), last(palette(I))), FIVE, ZERO)


def solve_ce9e57f2(I):
    return switch(fill(I, EIGHT, mapply(fork(connect, ulcorner,
        centerofmass), objects(I, T, F, T))), EIGHT, TWO)


def solve_22eb0ac0(I):
    return paint(I, mfilter(apply(fork(recolor, color, backdrop),
        fgpartition(I)), hline))


def solve_9f236235(I):
    return downscale(vmirror(compress(I)), valmin(objects(I, T, F, F), width))


def solve_a699fb00(I):
    return fill(I, TWO, intersection(shift(ofcolor(I, ONE), RIGHT), shift(
        ofcolor(I, ONE), LEFT)))


def solve_46442a0e(I):
    return vconcat(hconcat(I, rot90(I)), hconcat(rot270(I), rot180(I)))


def solve_7fe24cdd(I):
    return vconcat(hconcat(I, rot90(I)), hconcat(rot270(I), rot180(I)))


def solve_0ca9ddb6(I):
    return fill(fill(I, SEVEN, mapply(dneighbors, ofcolor(I, ONE))), FOUR,
        mapply(ineighbors, ofcolor(I, TWO)))


def solve_543a7ed5(I):
    return fill(fill(I, THREE, mapply(outbox, colorfilter(objects(I, T, F,
        T), SIX))), FOUR, mapply(delta, colorfilter(objects(I, T, F, T), SIX)))


def solve_0520fde7(I):
    return replace(cellwise(lefthalf(vmirror(I)), vmirror(righthalf(vmirror
        (I))), ZERO), ONE, TWO)


def solve_dae9d2b5(I):
    return fill(lefthalf(I), SIX, combine(ofcolor(lefthalf(I), FOUR),
        ofcolor(righthalf(I), THREE)))


def solve_8d5021e8(I):
    return hmirror(vconcat(vconcat(hconcat(vmirror(I), I), hmirror(hconcat(
        vmirror(I), I))), hconcat(vmirror(I), I)))


def solve_928ad970(I):
    return fill(I, leastcolor(trim(subgrid(ofcolor(I, FIVE), I))), inbox(
        ofcolor(I, FIVE)))


def solve_b60334d2(I):
    return fill(fill(replace(I, FIVE, ZERO), ONE, mapply(dneighbors,
        ofcolor(I, FIVE))), FIVE, mapply(ineighbors, ofcolor(I, FIVE)))


def solve_b94a9452(I):
    return switch(subgrid(first(objects(I, F, F, T)), I), leastcolor(
        subgrid(first(objects(I, F, F, T)), I)), mostcolor(subgrid(first(
        objects(I, F, F, T)), I)))


def solve_d037b0a7(I):
    return paint(I, mapply(fork(recolor, color, compose(rbind(shoot, DOWN),
        center)), objects(I, T, F, T)))


def solve_d0f5fe59(I):
    return fill(canvas(ZERO, astuple(size(objects(I, T, F, T)), size(
        objects(I, T, F, T)))), EIGHT, shoot(ORIGIN, UNITY))


def solve_e3497940(I):
    return paint(lefthalf(I), merge(objects(vmirror(righthalf(I)), T, F, T)))


def solve_e9afcf9a(I):
    return hconcat(hconcat(hconcat(crop(I, ORIGIN, astuple(TWO, ONE)),
        hmirror(crop(I, ORIGIN, astuple(TWO, ONE)))), hconcat(crop(I,
        ORIGIN, astuple(TWO, ONE)), hmirror(crop(I, ORIGIN, astuple(TWO,
        ONE))))), hconcat(crop(I, ORIGIN, astuple(TWO, ONE)), hmirror(crop(
        I, ORIGIN, astuple(TWO, ONE)))))


def solve_48d8fb45(I):
    return subgrid(extract(objects(I, T, T, T), lbind(adjacent, extract(
        objects(I, T, T, T), matcher(size, ONE)))), I)


def solve_d406998b(I):
    return vmirror(fill(vmirror(I), THREE, sfilter(ofcolor(vmirror(I), FIVE
        ), compose(even, last))))


def solve_5117e062(I):
    return replace(subgrid(extract(objects(I, F, T, T), matcher(numcolors,
        TWO)), I), EIGHT, mostcolor(extract(objects(I, F, T, T), matcher(
        numcolors, TWO))))


def solve_3906de3d(I):
    return cmirror(switch(apply(rbind(order, identity), switch(rot270(I),
        ONE, TWO)), ONE, TWO))


def solve_00d62c1b(I):
    return fill(I, FOUR, mfilter(colorfilter(objects(I, T, F, F), ZERO),
        compose(flip, rbind(bordering, I))))


def solve_7b6016b9(I):
    return replace(fill(I, TWO, mfilter(objects(I, T, F, F), compose(flip,
        rbind(bordering, I)))), ZERO, THREE)


def solve_67385a82(I):
    return fill(I, EIGHT, merge(difference(colorfilter(objects(I, T, F, F),
        THREE), sizefilter(colorfilter(objects(I, T, F, F), THREE), ONE))))


def solve_a5313dff(I):
    return fill(I, ONE, mfilter(colorfilter(objects(I, T, F, F), ZERO),
        compose(flip, rbind(bordering, I))))


def solve_ea32f347(I):
    return fill(fill(replace(I, FIVE, FOUR), ONE, argmax(objects(I, T, F, T
        ), size)), TWO, argmin(objects(I, T, F, T), size))


def solve_d631b094(I):
    return canvas(other(palette(I), ZERO), astuple(ONE, size(ofcolor(I,
        other(palette(I), ZERO)))))


def solve_10fcaaa3(I):
    return underfill(vconcat(hconcat(I, I), hconcat(I, I)), EIGHT, mapply(
        ineighbors, ofcolor(vconcat(hconcat(I, I), hconcat(I, I)),
        leastcolor(I))))


def solve_007bbfb7(I):
    return cellwise(vupscale(hupscale(I, THREE), THREE), vconcat(vconcat(
        hconcat(hconcat(I, I), I), hconcat(hconcat(I, I), I)), hconcat(
        hconcat(I, I), I)), ZERO)


def solve_496994bd(I):
    return vconcat(crop(I, ORIGIN, astuple(halve(height(I)), width(I))),
        hmirror(crop(I, ORIGIN, astuple(halve(height(I)), width(I)))))


def solve_1f876c06(I):
    return paint(I, mapply(fork(recolor, color, fork(connect, compose(last,
        first), power(last, TWO))), fgpartition(I)))


def solve_05f2a901(I):
    return move(I, first(colorfilter(objects(I, T, F, T), TWO)), gravitate(
        first(colorfilter(objects(I, T, F, T), TWO)), first(colorfilter(
        objects(I, T, F, T), EIGHT))))


def solve_39a8645d(I):
    return subgrid(extract(objects(I, T, T, T), matcher(color, mostcommon(
        apply(color, totuple(objects(I, T, T, T)))))), I)


def solve_1b2d62fb(I):
    return fill(replace(lefthalf(I), NINE, ZERO), EIGHT, intersection(
        ofcolor(lefthalf(I), ZERO), ofcolor(righthalf(I), ZERO)))


def solve_90c28cc7(I):
    return rot270(dedupe(rot90(dedupe(subgrid(first(objects(I, F, F, T)), I))))
        )


def solve_b6afb2da(I):
    return fill(fill(replace(I, FIVE, TWO), FOUR, mapply(box, colorfilter(
        objects(I, T, F, F), FIVE))), ONE, mapply(corners, colorfilter(
        objects(I, T, F, F), FIVE)))


def solve_b9b7f026(I):
    return canvas(color(extract(remove(argmin(objects(I, T, F, F), size),
        objects(I, T, F, F)), rbind(adjacent, argmin(objects(I, T, F, F),
        size)))), UNITY)


def solve_ba97ae07(I):
    return fill(I, mostcommon(apply(color, totuple(objects(I, T, F, T)))),
        backdrop(ofcolor(I, mostcommon(apply(color, totuple(objects(I, T, F,
        T)))))))


def solve_c9f8e694(I):
    return fill(hupscale(crop(I, ORIGIN, astuple(height(I), ONE)), width(I)
        ), ZERO, ofcolor(I, ZERO))


def solve_d23f8c26(I):
    return fill(I, ZERO, sfilter(asindices(I), compose(flip, matcher(last,
        halve(width(I))))))


def solve_d5d6de2d(I):
    return fill(replace(I, TWO, ZERO), THREE, mapply(compose(backdrop,
        inbox), difference(objects(I, T, F, T), sfilter(objects(I, T, F, T),
        square))))


def solve_dbc1a6ce(I):
    return underfill(I, EIGHT, mfilter(apply(fork(connect, first, last),
        product(ofcolor(I, ONE), ofcolor(I, ONE))), fork(either, vline, hline))
        )


def solve_ded97339(I):
    return underfill(I, EIGHT, mfilter(apply(fork(connect, first, last),
        product(ofcolor(I, EIGHT), ofcolor(I, EIGHT))), fork(either, vline,
        hline)))


def solve_ea786f4a(I):
    return fill(I, ZERO, combine(shoot(ORIGIN, UNITY), shoot(tojvec(
        decrement(width(I))), DOWN_LEFT)))


def solve_08ed6ac7(I):
    return paint(I, mpapply(recolor, interval(size(totuple(objects(I, T, F,
        T))), ZERO, NEG_ONE), order(objects(I, T, F, T), height)))


def solve_40853293(I):
    return paint(paint(I, mfilter(apply(fork(recolor, color, backdrop),
        partition(I)), hline)), mfilter(apply(fork(recolor, color, backdrop
        ), partition(I)), vline))


def solve_5521c0d9(I):
    return paint(cover(I, merge(objects(I, T, F, T))), mapply(fork(shift,
        identity, chain(toivec, invert, height)), objects(I, T, F, T)))


def solve_f8ff0b80(I):
    return hmirror(merge(apply(rbind(canvas, UNITY), apply(color, order(
        objects(I, T, T, T), size)))))


def solve_85c4e7cd(I):
    return paint(I, mpapply(recolor, apply(color, order(objects(I, T, F, F),
        compose(invert, size))), order(objects(I, T, F, F), size)))


def solve_d2abd087(I):
    return fill(fill(I, TWO, mfilter(objects(I, T, F, T), matcher(size, SIX
        ))), ONE, mfilter(objects(I, T, F, T), compose(flip, matcher(size,
        SIX))))


def solve_017c7c7b(I):
    return replace(vconcat(I, branch(equality(tophalf(I), bottomhalf(I)),
        bottomhalf(I), crop(I, TWO_BY_ZERO, THREE_BY_THREE))), ONE, TWO)


def solve_363442ee(I):
    return paint(I, mapply(compose(lbind(shift, asobject(crop(I, ORIGIN,
        THREE_BY_THREE))), decrement), ofcolor(I, ONE)))


def solve_5168d44c(I):
    return move(I, recolor(TWO, ofcolor(I, TWO)), branch(equality(height(
        ofcolor(I, THREE)), ONE), ZERO_BY_TWO, TWO_BY_ZERO))


def solve_e9614598(I):
    return fill(I, THREE, insert(halve(apply_func(fork(add, first, last),
        ofcolor(I, ONE))), dneighbors(halve(apply_func(fork(add, first,
        last), ofcolor(I, ONE))))))


def solve_d9fac9be(I):
    return canvas(other(remove(ZERO, palette(I)), color(argmax(objects(I, T,
        F, T), size))), UNITY)


def solve_e50d258f(I):
    return subgrid(argmax(objects(vconcat(I, canvas(ZERO, astuple(NINE,
        width(I)))), F, F, T), rbind(colorcount, TWO)), I)


def solve_810b9b61(I):
    return fill(I, THREE, mfilter(difference(apply(toindices, objects(I, T,
        T, T)), sfilter(apply(toindices, objects(I, T, T, T)), fork(either,
        vline, hline))), fork(equality, identity, box)))


def solve_54d82841(I):
    return fill(I, FOUR, apply(lbind(astuple, decrement(height(I))), apply(
        compose(last, center), objects(I, T, F, T))))


def solve_60b61512(I):
    return fill(I, SEVEN, mapply(delta, objects(I, T, T, T)))


def solve_25d8a9c8(I):
    return fill(fill(I, FIVE, toindices(mfilter(sizefilter(objects(I, T, F,
        F), THREE), hline))), ZERO, difference(asindices(I), toindices(
        mfilter(sizefilter(objects(I, T, F, F), THREE), hline))))


def solve_239be575(I):
    return canvas(branch(greater(size(sfilter(objects(I, F, T, T), compose(
        lbind(contained, TWO), palette))), ONE), ZERO, EIGHT), UNITY)


def solve_67a423a3(I):
    return fill(I, FOUR, neighbors(first(delta(merge(colorfilter(objects(I,
        T, F, T), leastcolor(I)))))))


def solve_5c0a986e(I):
    return fill(fill(I, TWO, shoot(lrcorner(ofcolor(I, TWO)), UNITY)), ONE,
        shoot(ulcorner(ofcolor(I, ONE)), NEG_UNITY))


def solve_6430c8c4(I):
    return fill(canvas(ZERO, astuple(FOUR, FOUR)), THREE, intersection(
        ofcolor(tophalf(I), ZERO), ofcolor(bottomhalf(I), ZERO)))


def solve_94f9d214(I):
    return fill(canvas(ZERO, astuple(FOUR, FOUR)), TWO, intersection(
        ofcolor(tophalf(I), ZERO), ofcolor(bottomhalf(I), ZERO)))


def solve_a1570a43(I):
    return move(I, recolor(TWO, ofcolor(I, TWO)), increment(subtract(
        ulcorner(ofcolor(I, THREE)), ulcorner(ofcolor(I, TWO)))))


def solve_ce4f8723(I):
    return fill(canvas(THREE, astuple(FOUR, FOUR)), ZERO, intersection(
        ofcolor(tophalf(I), ZERO), ofcolor(bottomhalf(I), ZERO)))


def solve_d13f3404(I):
    return paint(canvas(ZERO, astuple(SIX, SIX)), mapply(fork(recolor,
        color, compose(rbind(shoot, UNITY), center)), objects(I, T, F, T)))


def solve_dc433765(I):
    return move(I, recolor(THREE, ofcolor(I, THREE)), sign(subtract(first(
        ofcolor(I, FOUR)), first(ofcolor(I, THREE)))))


def solve_f2829549(I):
    return fill(canvas(ZERO, shape(lefthalf(I))), THREE, intersection(
        ofcolor(lefthalf(I), ZERO), ofcolor(righthalf(I), ZERO)))


def solve_fafffa47(I):
    return fill(canvas(ZERO, shape(bottomhalf(I))), TWO, intersection(
        ofcolor(tophalf(I), ZERO), ofcolor(bottomhalf(I), ZERO)))


def solve_fcb5c309(I):
    return replace(subgrid(argmax(difference(objects(I, T, F, T),
        colorfilter(objects(I, T, F, T), leastcolor(I))), size), I), color(
        argmax(difference(objects(I, T, F, T), colorfilter(objects(I, T, F,
        T), leastcolor(I))), size)), leastcolor(I))


def solve_ff805c23(I):
    return branch(contained(ONE, palette(subgrid(ofcolor(I, ONE), hmirror(I
        )))), subgrid(ofcolor(I, ONE), vmirror(I)), subgrid(ofcolor(I, ONE),
        hmirror(I)))


def solve_e76a88a6(I):
    return paint(I, mapply(lbind(shift, normalize(argmax(objects(I, F, F, T
        ), numcolors))), apply(ulcorner, remove(argmax(objects(I, F, F, T),
        numcolors), objects(I, F, F, T)))))


def solve_7c008303(I):
    return fill(upscale(compress(replace(replace(I, THREE, ZERO), EIGHT,
        ZERO)), THREE), ZERO, ofcolor(subgrid(ofcolor(I, THREE), I), ZERO))


def solve_7f4411dc(I):
    return fill(I, ZERO, sfilter(ofcolor(I, leastcolor(I)), compose(chain(
        rbind(greater, TWO), size, rbind(difference, ofcolor(I, leastcolor(
        I)))), dneighbors)))


def solve_b230c067(I):
    return fill(replace(I, EIGHT, ONE), TWO, extract(objects(I, T, T, T),
        matcher(normalize, leastcommon(apply(normalize, totuple(objects(I,
        T, T, T)))))))


def solve_e8593010(I):
    return replace(fill(fill(I, THREE, merge(sizefilter(objects(I, T, F, T),
        ONE))), TWO, merge(sizefilter(objects(I, T, F, T), TWO))), ZERO, ONE)


def solve_6d75e8bb(I):
    return paint(I, shift(asobject(replace(subgrid(first(objects(I, T, F, T
        )), I), ZERO, TWO)), ulcorner(first(objects(I, T, F, T)))))


def solve_3f7978a0(I):
    return crop(I, subtract(ulcorner(extract(fgpartition(I), matcher(color,
        FIVE))), DOWN), add(shape(extract(fgpartition(I), matcher(color,
        FIVE))), TWO_BY_ZERO))


def solve_1190e5a7(I):
    return canvas(mostcolor(I), increment(apply(size, astuple(difference(
        frontiers(I), sfilter(frontiers(I), vline)), sfilter(frontiers(I),
        vline)))))


def solve_6e02f1e3(I):
    return fill(canvas(ZERO, THREE_BY_THREE), FIVE, connect(branch(equality
        (numcolors(I), THREE), TWO_BY_ZERO, ORIGIN), branch(equality(
        numcolors(I), TWO), TWO_BY_TWO, ZERO_BY_TWO)))


def solve_a61f2674(I):
    return paint(replace(I, FIVE, ZERO), combine(recolor(ONE, argmax(
        objects(I, T, F, T), size)), recolor(TWO, argmin(objects(I, T, F, T
        ), size))))


def solve_fcc82909(I):
    return fill(I, THREE, mapply(compose(box, fork(astuple, compose(rbind(
        add, DOWN), llcorner), fork(add, lrcorner, compose(toivec,
        numcolors)))), objects(I, F, T, T)))


def solve_72ca375d(I):
    return first(extract(pair(apply(rbind(subgrid, I), totuple(objects(I, T,
        T, T))), papply(equality, apply(rbind(subgrid, I), totuple(objects(
        I, T, T, T))), apply(vmirror, apply(rbind(subgrid, I), totuple(
        objects(I, T, T, T)))))), last))


def solve_253bf280(I):
    return fill(fill(I, THREE, mfilter(sfilter(prapply(connect, ofcolor(I,
        EIGHT), ofcolor(I, EIGHT)), compose(rbind(greater, ONE), size)),
        fork(either, vline, hline))), EIGHT, ofcolor(I, EIGHT))


def solve_694f12f3(I):
    return fill(fill(I, ONE, apply_func(compose(backdrop, inbox), argmin(
        colorfilter(objects(I, T, F, F), FOUR), size))), TWO, apply_func(
        compose(backdrop, inbox), argmax(colorfilter(objects(I, T, F, F),
        FOUR), size)))


def solve_1f642eb9(I):
    return paint(I, mapply(fork(shift, identity, compose(crement, rbind(
        gravitate, first(difference(objects(I, T, F, T), sizefilter(objects
        (I, T, F, T), ONE)))))), sizefilter(objects(I, T, F, T), ONE)))


def solve_31aa019c(I):
    return fill(fill(canvas(ZERO, astuple(TEN, TEN)), leastcolor(I),
        initset(first(ofcolor(I, leastcolor(I))))), TWO, neighbors(first(
        ofcolor(I, leastcolor(I)))))


def solve_27a28665(I):
    return canvas(branch(equality(valmax(objects(I, T, F, F), size), FIVE),
        SIX, branch(equality(valmax(objects(I, T, F, F), size), FOUR),
        THREE, branch(equality(valmax(objects(I, T, F, F), size), ONE), TWO,
        ONE))), UNITY)


def solve_7ddcd7ec(I):
    return fill(I, color(first(difference(objects(I, T, F, T), sizefilter(
        objects(I, T, F, T), ONE)))), mapply(fork(shoot, center, lbind(
        position, first(difference(objects(I, T, F, T), sizefilter(objects(
        I, T, F, T), ONE))))), sizefilter(objects(I, T, F, T), ONE)))


def solve_3bd67248(I):
    return fill(fill(I, TWO, shoot(astuple(decrement(decrement(height(I))),
        ONE), UP_RIGHT)), FOUR, shoot(astuple(decrement(height(I)), ONE),
        RIGHT))


def solve_73251a56(I):
    return fill(replace(apply(lbind(apply, maximum), papply(pair, I,
        dmirror(I))), ZERO, mostcolor(apply(lbind(apply, maximum), papply(
        pair, I, dmirror(I))))), index(replace(apply(lbind(apply, maximum),
        papply(pair, I, dmirror(I))), ZERO, mostcolor(apply(lbind(apply,
        maximum), papply(pair, I, dmirror(I))))), ORIGIN), shoot(ORIGIN, UNITY)
        )


def solve_25d487eb(I):
    return underfill(I, leastcolor(I), shoot(center(ofcolor(I, leastcolor(I
        ))), subtract(center(merge(objects(I, T, F, T))), center(ofcolor(I,
        leastcolor(I))))))


def solve_8f2ea7aa(I):
    return cellwise(upscale(subgrid(merge(objects(I, T, F, T)), I), THREE),
        vconcat(vconcat(hconcat(hconcat(subgrid(merge(objects(I, T, F, T)),
        I), subgrid(merge(objects(I, T, F, T)), I)), subgrid(merge(objects(
        I, T, F, T)), I)), hconcat(hconcat(subgrid(merge(objects(I, T, F, T
        )), I), subgrid(merge(objects(I, T, F, T)), I)), subgrid(merge(
        objects(I, T, F, T)), I))), hconcat(hconcat(subgrid(merge(objects(I,
        T, F, T)), I), subgrid(merge(objects(I, T, F, T)), I)), subgrid(
        merge(objects(I, T, F, T)), I))), ZERO)


def solve_b8825c91(I):
    return cmirror(apply(lbind(apply, maximum), papply(pair, apply(lbind(
        apply, maximum), papply(pair, replace(I, FOUR, ZERO), dmirror(
        replace(I, FOUR, ZERO)))), cmirror(apply(lbind(apply, maximum),
        papply(pair, replace(I, FOUR, ZERO), dmirror(replace(I, FOUR, ZERO)
        )))))))


def solve_cce03e0d(I):
    return fill(vconcat(vconcat(hconcat(hconcat(I, I), I), hconcat(hconcat(
        I, I), I)), hconcat(hconcat(I, I), I)), ZERO, combine(ofcolor(
        upscale(I, THREE), ZERO), ofcolor(upscale(I, THREE), ONE)))


def solve_d364b489(I):
    return fill(fill(fill(fill(I, EIGHT, shift(ofcolor(I, ONE), DOWN)), TWO,
        shift(ofcolor(I, ONE), UP)), SIX, shift(ofcolor(I, ONE), RIGHT)),
        SEVEN, shift(ofcolor(I, ONE), LEFT))


def solve_a5f85a15(I):
    return fill(I, FOUR, mapply(lbind(shift, papply(astuple, apply(
        decrement, apply(double, interval(ONE, NINE, ONE))), apply(
        decrement, apply(double, interval(ONE, NINE, ONE))))), apply(
        ulcorner, objects(I, T, T, T))))


def solve_3ac3eb23(I):
    return vconcat(first(vsplit(paint(I, mapply(fork(recolor, color, chain(
        ineighbors, last, first)), objects(I, T, F, T))), THREE)), vconcat(
        first(vsplit(paint(I, mapply(fork(recolor, color, chain(ineighbors,
        last, first)), objects(I, T, F, T))), THREE)), first(vsplit(paint(I,
        mapply(fork(recolor, color, chain(ineighbors, last, first)),
        objects(I, T, F, T))), THREE))))


def solve_444801d8(I):
    return underpaint(I, mapply(fork(recolor, chain(leastcolor, rbind(
        toobject, I), delta), compose(rbind(shift, UP), backdrop)),
        colorfilter(objects(I, T, F, T), ONE)))


def solve_22168020(I):
    return paint(I, mapply(fork(recolor, identity, compose(merge, fork(
        lbind(prapply, connect), lbind(ofcolor, I), lbind(ofcolor, I)))),
        remove(ZERO, palette(I))))


def solve_6e82a1ae(I):
    return fill(fill(fill(I, THREE, apply_func(compose(merge, lbind(
        sizefilter, objects(I, T, F, T))), TWO)), TWO, apply_func(compose(
        merge, lbind(sizefilter, objects(I, T, F, T))), THREE)), ONE,
        apply_func(compose(merge, lbind(sizefilter, objects(I, T, F, T))),
        FOUR))


def solve_b2862040(I):
    return fill(I, EIGHT, mfilter(colorfilter(objects(I, T, F, F), ONE),
        rbind(adjacent, mfilter(colorfilter(objects(I, T, F, F), NINE),
        compose(flip, rbind(bordering, I))))))


def solve_868de0fa(I):
    return fill(fill(I, TWO, merge(sfilter(sfilter(objects(I, T, F, F),
        square), compose(even, height)))), SEVEN, merge(difference(sfilter(
        objects(I, T, F, F), square), sfilter(sfilter(objects(I, T, F, F),
        square), compose(even, height)))))


def solve_681b3aeb(I):
    return rot90(paint(canvas(color(argmin(objects(rot270(I), T, F, T),
        size)), THREE_BY_THREE), normalize(argmax(objects(rot270(I), T, F,
        T), size))))


def solve_8e5a5113(I):
    return paint(I, mpapply(shift, apply(asobject, astuple(rot90(crop(I,
        ORIGIN, THREE_BY_THREE)), rot180(crop(I, ORIGIN, THREE_BY_THREE)))),
        apply(tojvec, astuple(FOUR, EIGHT))))


def solve_025d127b(I):
    return move(I, difference(merge(objects(I, T, F, T)), mapply(compose(
        rbind(argmax, rightmost), lbind(colorfilter, objects(I, T, F, T))),
        apply(color, objects(I, T, F, T)))), RIGHT)


def solve_2281f1f4(I):
    return underfill(I, TWO, remove(urcorner(ofcolor(I, FIVE)), apply(fork(
        astuple, power(first, TWO), power(last, TWO)), product(ofcolor(I,
        FIVE), ofcolor(I, FIVE)))))


def solve_cf98881b(I):
    return fill(fill(last(remove(first(hsplit(I, THREE)), hsplit(I, THREE))
        ), NINE, ofcolor(first(remove(first(hsplit(I, THREE)), hsplit(I,
        THREE))), NINE)), FOUR, ofcolor(first(hsplit(I, THREE)), FOUR))


def solve_d4f3cd78(I):
    return fill(fill(I, EIGHT, delta(ofcolor(I, FIVE))), EIGHT, shoot(first
        (difference(box(ofcolor(I, FIVE)), ofcolor(I, FIVE))), position(box
        (ofcolor(I, FIVE)), difference(box(ofcolor(I, FIVE)), ofcolor(I,
        FIVE)))))


def solve_bda2d7a6(I):
    return paint(I, mpapply(recolor, apply(color, order(partition(I), size)
        ), combine(repeat(last(order(partition(I), size)), ONE), remove(
        last(order(partition(I), size)), order(partition(I), size)))))


def solve_137eaa0f(I):
    return paint(canvas(ZERO, THREE_BY_THREE), shift(mapply(fork(shift,
        identity, chain(invert, center, rbind(sfilter, matcher(first, FIVE)
        ))), objects(I, F, T, T)), UNITY))


def solve_6455b5f5(I):
    return fill(paint(I, recolor(ONE, argmax(objects(I, T, F, F), size))),
        EIGHT, merge(sizefilter(colorfilter(objects(I, T, F, F), ZERO),
        valmin(objects(I, T, F, F), size))))


def solve_b8cdaf2b(I):
    return underfill(I, leastcolor(I), combine(shoot(ulcorner(shift(ofcolor
        (I, leastcolor(I)), UP)), NEG_UNITY), shoot(urcorner(shift(ofcolor(
        I, leastcolor(I)), UP)), UP_RIGHT)))


def solve_bd4472b8(I):
    return vconcat(crop(I, ORIGIN, astuple(TWO, width(I))), merge(repeat(
        hupscale(dmirror(tophalf(crop(I, ORIGIN, astuple(TWO, width(I))))),
        width(I)), TWO)))


def solve_4be741c5(I):
    return apply_func(branch(portrait(I), dmirror, identity), apply(dedupe,
        crop(apply_func(branch(portrait(I), dmirror, identity), I), ORIGIN,
        astuple(ONE, apply_func(branch(portrait(I), height, width), I)))))


def solve_bbc9ae5d(I):
    return fill(vupscale(I, halve(width(I))), other(palette(I), ZERO),
        mapply(rbind(shoot, UNITY), ofcolor(vupscale(I, halve(width(I))),
        other(palette(I), ZERO))))


def solve_d90796e8(I):
    return fill(cover(I, mfilter(sizefilter(objects(I, F, F, T), TWO),
        compose(lbind(contained, TWO), palette))), EIGHT, sfilter(mfilter(
        sizefilter(objects(I, F, F, T), TWO), compose(lbind(contained, TWO),
        palette)), matcher(first, THREE)))


def solve_2c608aff(I):
    return underfill(I, leastcolor(I), mfilter(prapply(connect, toindices(
        argmax(objects(I, T, F, T), size)), ofcolor(I, leastcolor(I))),
        fork(either, vline, hline)))


def solve_f8b3ba0a(I):
    return crop(merge(apply(rbind(canvas, UNITY), order(palette(compress(I)
        ), compose(invert, lbind(colorcount, compress(I)))))), DOWN,
        astuple(THREE, ONE))


def solve_80af3007(I):
    return downscale(cellwise(upscale(subgrid(first(objects(I, T, T, T)), I
        ), THREE), vconcat(vconcat(hconcat(hconcat(subgrid(first(objects(I,
        T, T, T)), I), subgrid(first(objects(I, T, T, T)), I)), subgrid(
        first(objects(I, T, T, T)), I)), hconcat(hconcat(subgrid(first(
        objects(I, T, T, T)), I), subgrid(first(objects(I, T, T, T)), I)),
        subgrid(first(objects(I, T, T, T)), I))), hconcat(hconcat(subgrid(
        first(objects(I, T, T, T)), I), subgrid(first(objects(I, T, T, T)),
        I)), subgrid(first(objects(I, T, T, T)), I))), ZERO), THREE)


def solve_83302e8f(I):
    return paint(paint(I, recolor(THREE, merge(sfilter(colorfilter(objects(
        I, T, F, F), ZERO), square)))), recolor(FOUR, merge(difference(
        colorfilter(objects(I, T, F, F), ZERO), sfilter(colorfilter(objects
        (I, T, F, F), ZERO), square)))))


def solve_1fad071e(I):
    return hconcat(canvas(ONE, astuple(ONE, size(sizefilter(colorfilter(
        objects(I, T, F, T), ONE), FOUR)))), canvas(ZERO, astuple(ONE,
        subtract(FIVE, size(sizefilter(colorfilter(objects(I, T, F, T), ONE
        ), FOUR))))))


def solve_11852cab(I):
    return paint(paint(paint(paint(I, hmirror(merge(objects(I, T, T, T)))),
        vmirror(merge(objects(I, T, T, T)))), dmirror(merge(objects(I, T, T,
        T)))), cmirror(merge(objects(I, T, T, T))))


def solve_3428a4f5(I):
    return fill(canvas(ZERO, astuple(SIX, FIVE)), THREE, difference(combine
        (ofcolor(tophalf(I), TWO), ofcolor(bottomhalf(I), TWO)),
        intersection(ofcolor(tophalf(I), TWO), ofcolor(bottomhalf(I), TWO))))


def solve_178fcbfb(I):
    return paint(fill(I, TWO, mapply(vfrontier, ofcolor(I, TWO))), mapply(
        fork(recolor, color, compose(hfrontier, center)), difference(
        objects(I, T, F, T), colorfilter(objects(I, T, F, T), TWO))))


def solve_3de23699(I):
    return replace(trim(subgrid(first(sizefilter(fgpartition(I), FOUR)), I)
        ), color(first(difference(fgpartition(I), sizefilter(fgpartition(I),
        FOUR)))), color(first(sizefilter(fgpartition(I), FOUR))))


def solve_54d9e175(I):
    return replace(replace(replace(replace(paint(I, mapply(fork(recolor,
        color, compose(neighbors, center)), sizefilter(objects(I, T, F, T),
        ONE))), ONE, SIX), TWO, SEVEN), THREE, EIGHT), FOUR, NINE)


def solve_5ad4f10b(I):
    return downscale(replace(replace(subgrid(argmax(objects(I, T, T, T),
        size), I), leastcolor(subgrid(argmax(objects(I, T, T, T), size), I)
        ), ZERO), color(argmax(objects(I, T, T, T), size)), leastcolor(
        subgrid(argmax(objects(I, T, T, T), size), I))), divide(height(
        replace(replace(subgrid(argmax(objects(I, T, T, T), size), I),
        leastcolor(subgrid(argmax(objects(I, T, T, T), size), I)), ZERO),
        color(argmax(objects(I, T, T, T), size)), leastcolor(subgrid(argmax
        (objects(I, T, T, T), size), I)))), THREE))


def solve_623ea044(I):
    return fill(I, color(first(objects(I, T, F, T))), mapply(lbind(shoot,
        center(first(objects(I, T, F, T)))), combine(astuple(UNITY,
        NEG_UNITY), astuple(UP_RIGHT, DOWN_LEFT))))


def solve_6b9890af(I):
    return paint(subgrid(ofcolor(I, TWO), I), shift(normalize(upscale(
        argmin(objects(I, T, T, T), size), divide(width(subgrid(ofcolor(I,
        TWO), I)), THREE))), UNITY))


def solve_794b24be(I):
    return fill(canvas(ZERO, THREE_BY_THREE), TWO, branch(equality(size(
        ofcolor(I, ONE)), FOUR), insert(UNITY, connect(ORIGIN, tojvec(
        decrement(size(ofcolor(I, ONE)))))), connect(ORIGIN, tojvec(
        decrement(size(ofcolor(I, ONE)))))))


def solve_88a10436(I):
    return paint(I, shift(shift(normalize(first(difference(objects(I, F, F,
        T), colorfilter(objects(I, F, F, T), FIVE)))), center(first(
        colorfilter(objects(I, F, F, T), FIVE)))), NEG_UNITY))


def solve_88a62173(I):
    return leastcommon(combine(astuple(tophalf(lefthalf(I)), tophalf(
        righthalf(I))), astuple(bottomhalf(lefthalf(I)), bottomhalf(
        righthalf(I)))))


def solve_890034e9(I):
    return fill(I, leastcolor(I), mapply(lbind(shift, shift(normalize(
        ofcolor(I, leastcolor(I))), NEG_UNITY)), occurrences(I, recolor(
        ZERO, inbox(ofcolor(I, leastcolor(I)))))))


def solve_99b1bc43(I):
    return fill(canvas(ZERO, shape(tophalf(I))), THREE, difference(combine(
        ofcolor(tophalf(I), ZERO), ofcolor(bottomhalf(I), ZERO)),
        intersection(ofcolor(tophalf(I), ZERO), ofcolor(bottomhalf(I), ZERO))))


def solve_a9f96cdd(I):
    return fill(fill(fill(fill(replace(I, TWO, ZERO), THREE, shift(ofcolor(
        I, TWO), NEG_UNITY)), SIX, shift(ofcolor(I, TWO), UP_RIGHT)), EIGHT,
        shift(ofcolor(I, TWO), DOWN_LEFT)), SEVEN, shift(ofcolor(I, TWO),
        UNITY))


def solve_af902bf9(I):
    return replace(fill(underfill(I, NEG_ONE, mfilter(prapply(connect,
        ofcolor(I, FOUR), ofcolor(I, FOUR)), fork(either, vline, hline))),
        TWO, mapply(compose(backdrop, inbox), objects(underfill(I, NEG_ONE,
        mfilter(prapply(connect, ofcolor(I, FOUR), ofcolor(I, FOUR)), fork(
        either, vline, hline))), F, F, T))), NEG_ONE, ZERO)


def solve_b548a754(I):
    return fill(fill(I, leastcolor(replace(I, EIGHT, ZERO)), backdrop(merge
        (objects(I, T, F, T)))), leastcolor(replace(replace(I, EIGHT, ZERO),
        leastcolor(replace(I, EIGHT, ZERO)), ZERO)), box(merge(objects(I, T,
        F, T))))


def solve_bdad9b1f(I):
    return fill(fill(fill(I, TWO, hfrontier(center(ofcolor(I, TWO)))),
        EIGHT, vfrontier(center(ofcolor(I, EIGHT)))), FOUR, intersection(
        hfrontier(center(ofcolor(I, TWO))), vfrontier(center(ofcolor(I,
        EIGHT)))))


def solve_c3e719e8(I):
    return fill(vconcat(vconcat(hconcat(hconcat(I, I), I), hconcat(hconcat(
        I, I), I)), hconcat(hconcat(I, I), I)), ZERO, difference(asindices(
        upscale(I, THREE)), ofcolor(upscale(I, THREE), mostcolor(I))))


def solve_de1cd16c(I):
    return canvas(mostcolor(argmax(apply(rbind(subgrid, I), difference(
        objects(I, T, F, F), sizefilter(objects(I, T, F, F), ONE))), rbind(
        colorcount, leastcolor(I)))), UNITY)


def solve_d8c310e9(I):
    return paint(paint(I, shift(first(objects(I, F, F, T)), tojvec(hperiod(
        first(objects(I, F, F, T)))))), shift(first(objects(I, F, F, T)),
        tojvec(multiply(hperiod(first(objects(I, F, F, T))), THREE))))


def solve_a3325580(I):
    return dmirror(merge(apply(rbind(canvas, astuple(ONE, valmax(objects(I,
        T, F, T), size))), apply(color, order(sizefilter(objects(I, T, F, T
        ), valmax(objects(I, T, F, T), size)), leftmost)))))


def solve_8eb1be9a(I):
    return paint(I, mapply(lbind(shift, first(objects(I, T, T, T))), apply(
        toivec, apply(rbind(multiply, height(first(objects(I, T, T, T)))),
        interval(NEG_TWO, FOUR, ONE)))))


def solve_321b1fc6(I):
    return paint(cover(I, first(difference(objects(I, F, F, T), colorfilter
        (objects(I, F, F, T), EIGHT)))), mapply(lbind(shift, normalize(
        first(difference(objects(I, F, F, T), colorfilter(objects(I, F, F,
        T), EIGHT))))), apply(ulcorner, colorfilter(objects(I, F, F, T),
        EIGHT))))


def solve_1caeab9d(I):
    return paint(cover(I, merge(objects(I, T, T, T))), mapply(fork(shift,
        identity, chain(toivec, lbind(subtract, lowermost(ofcolor(I, ONE))),
        lowermost)), objects(I, T, T, T)))


def solve_77fdfe62(I):
    return fill(upscale(compress(replace(replace(I, EIGHT, ZERO), ONE, ZERO
        )), halve(width(subgrid(ofcolor(I, EIGHT), I)))), ZERO, ofcolor(
        subgrid(ofcolor(I, EIGHT), I), ZERO))


def solve_c0f76784(I):
    return fill(fill(fill(I, SEVEN, merge(sfilter(colorfilter(objects(I, T,
        F, F), ZERO), square))), EIGHT, argmax(sfilter(colorfilter(objects(
        I, T, F, F), ZERO), square), size)), SIX, merge(sizefilter(sfilter(
        colorfilter(objects(I, T, F, F), ZERO), square), ONE)))


def solve_1b60fb0c(I):
    return underfill(I, TWO, argmax(apply(lbind(shift, ofcolor(rot90(I),
        ONE)), mapply(neighbors, neighbors(ORIGIN))), compose(size, lbind(
        intersection, ofcolor(I, ONE)))))


def solve_ddf7fa4f(I):
    return paint(I, mapply(fork(recolor, compose(color, first), last),
        sfilter(product(sizefilter(objects(I, T, F, T), ONE), colorfilter(
        objects(I, T, F, T), FIVE)), fork(vmatching, first, last))))


def solve_47c1f68c(I):
    return replace(compress(cellwise(cellwise(I, vmirror(I), leastcolor(I)),
        hmirror(cellwise(I, vmirror(I), leastcolor(I))), leastcolor(I))),
        leastcolor(I), mostcolor(merge(objects(I, T, T, T))))


def solve_6c434453(I):
    return fill(cover(I, merge(sizefilter(objects(I, T, F, T), EIGHT))),
        TWO, mapply(lbind(shift, insert(UNITY, dneighbors(UNITY))), apply(
        ulcorner, sizefilter(objects(I, T, F, T), EIGHT))))


def solve_23581191(I):
    return fill(paint(I, mapply(fork(recolor, color, compose(fork(combine,
        vfrontier, hfrontier), center)), objects(I, T, T, T))), TWO,
        apply_func(fork(intersection, first, last), apply(compose(fork(
        combine, vfrontier, hfrontier), center), objects(I, T, T, T))))


def solve_c8cbb738(I):
    return paint(canvas(mostcolor(I), valmax(fgpartition(I), shape)),
        mapply(fork(shift, identity, chain(halve, lbind(subtract, valmax(
        fgpartition(I), shape)), shape)), apply(normalize, fgpartition(I))))


def solve_3eda0437(I):
    return fill(I, SIX, argmax(mapply(chain(fork(apply, lbind(lbind, shift),
        lbind(occurrences, I)), asobject, lbind(canvas, ZERO)), prapply(
        astuple, interval(TWO, TEN, ONE), interval(TWO, TEN, ONE))), size))


def solve_dc0a314f(I):
    return subgrid(ofcolor(I, THREE), apply(lbind(apply, maximum), papply(
        pair, apply(lbind(apply, maximum), papply(pair, replace(I, THREE,
        ZERO), dmirror(replace(I, THREE, ZERO)))), cmirror(apply(lbind(
        apply, maximum), papply(pair, replace(I, THREE, ZERO), dmirror(
        replace(I, THREE, ZERO))))))))


def solve_d4469b4b(I):
    return fill(canvas(ZERO, THREE_BY_THREE), FIVE, apply_func(fork(combine,
        vfrontier, hfrontier), branch(equality(other(palette(I), ZERO), TWO
        ), RIGHT, branch(equality(other(palette(I), ZERO), ONE), UNITY,
        TWO_BY_TWO))))


def solve_6ecd11f4(I):
    return fill(subgrid(argmin(objects(I, F, T, T), size), I), ZERO,
        ofcolor(downscale(subgrid(argmax(objects(I, F, T, T), size), I),
        divide(width(subgrid(argmax(objects(I, F, T, T), size), I)), width(
        subgrid(argmin(objects(I, F, T, T), size), I)))), ZERO))


def solve_760b3cac(I):
    return fill(I, EIGHT, shift(vmirror(ofcolor(I, EIGHT)), tojvec(multiply
        (branch(equality(index(I, ulcorner(ofcolor(I, FOUR))), FOUR),
        NEG_ONE, ONE), THREE))))


def solve_c444b776(I):
    return paint(I, mapply(compose(lbind(shift, normalize(toobject(backdrop
        (argmin(colorfilter(objects(I, T, F, F), ZERO), size)), I))),
        ulcorner), colorfilter(objects(I, T, F, F), ZERO)))


def solve_d4a91cb9(I):
    return underfill(I, FOUR, combine(connect(astuple(first(first(ofcolor(I,
        TWO))), last(first(ofcolor(I, EIGHT)))), first(ofcolor(I, EIGHT))),
        connect(astuple(first(first(ofcolor(I, TWO))), last(first(ofcolor(I,
        EIGHT)))), first(ofcolor(I, TWO)))))


def solve_eb281b96(I):
    return vconcat(vconcat(I, hmirror(crop(I, ORIGIN, astuple(decrement(
        height(I)), width(I))))), crop(vconcat(I, hmirror(crop(I, ORIGIN,
        astuple(decrement(height(I)), width(I))))), DOWN, astuple(double(
        decrement(height(I))), width(I))))


def solve_ff28f65a(I):
    return merge(hsplit(fill(canvas(ZERO, astuple(ONE, NINE)), ONE, apply(
        tojvec, interval(ZERO, double(size(objects(I, T, F, T))), TWO))),
        THREE))


def solve_7e0986d6(I):
    return fill(replace(I, leastcolor(I), ZERO), leastcolor(replace(I,
        leastcolor(I), ZERO)), sfilter(ofcolor(I, leastcolor(I)), chain(
        chain(positive, decrement, rbind(colorcount, leastcolor(replace(I,
        leastcolor(I), ZERO)))), rbind(toobject, replace(I, leastcolor(I),
        ZERO)), dneighbors)))


def solve_09629e4f(I):
    return fill(paint(I, upscale(normalize(argmin(objects(I, F, T, T),
        numcolors)), FOUR)), FIVE, ofcolor(I, FIVE))


def solve_a85d4709(I):
    return fill(fill(fill(I, TWO, apply_func(chain(lbind(mapply, hfrontier),
        lbind(sfilter, ofcolor(I, FIVE)), lbind(matcher, last)), ZERO)),
        THREE, apply_func(chain(lbind(mapply, hfrontier), lbind(sfilter,
        ofcolor(I, FIVE)), lbind(matcher, last)), TWO)), FOUR, apply_func(
        chain(lbind(mapply, hfrontier), lbind(sfilter, ofcolor(I, FIVE)),
        lbind(matcher, last)), ONE))


def solve_feca6190(I):
    return hmirror(paint(canvas(ZERO, astuple(multiply(size(objects(I, T, F,
        T)), FIVE), multiply(size(objects(I, T, F, T)), FIVE))), mapply(
        fork(recolor, color, compose(rbind(shoot, UNITY), center)), objects
        (I, T, F, T))))


def solve_a68b268e(I):
    return fill(fill(fill(righthalf(bottomhalf(I)), EIGHT, ofcolor(lefthalf
        (bottomhalf(I)), EIGHT)), FOUR, ofcolor(righthalf(tophalf(I)), FOUR
        )), SEVEN, ofcolor(lefthalf(tophalf(I)), SEVEN))


def solve_beb8660c(I):
    return rot180(paint(canvas(ZERO, shape(I)), mpapply(shift, apply(
        normalize, order(objects(I, T, F, T), compose(invert, size))),
        apply(toivec, interval(ZERO, size(apply(normalize, order(objects(I,
        T, F, T), compose(invert, size)))), ONE)))))


def solve_913fb3ed(I):
    return fill(fill(fill(I, SIX, mapply(neighbors, ofcolor(I, THREE))),
        FOUR, mapply(neighbors, ofcolor(I, EIGHT))), ONE, mapply(neighbors,
        ofcolor(I, TWO)))


def solve_0962bcdd(I):
    return fill(fill(I, leastcolor(replace(I, ZERO, leastcolor(I))), mapply
        (dneighbors, ofcolor(I, leastcolor(replace(I, ZERO, leastcolor(I)))
        ))), leastcolor(I), mapply(fork(combine, fork(connect, ulcorner,
        lrcorner), fork(connect, llcorner, urcorner)), objects(fill(I,
        leastcolor(replace(I, ZERO, leastcolor(I))), mapply(dneighbors,
        ofcolor(I, leastcolor(replace(I, ZERO, leastcolor(I)))))), F, T, T)))


def solve_3631a71a(I):
    return paint(apply(lbind(apply, maximum), papply(pair, replace(I, NINE,
        ZERO), dmirror(replace(I, NINE, ZERO)))), shift(merge(objects(
        vmirror(crop(apply(lbind(apply, maximum), papply(pair, replace(I,
        NINE, ZERO), dmirror(replace(I, NINE, ZERO)))), TWO_BY_TWO,
        subtract(shape(I), TWO_BY_TWO))), T, F, T)), TWO_BY_TWO))


def solve_05269061(I):
    return paint(paint(paint(I, mapply(lbind(shift, merge(objects(I, T, T,
        T))), apply(rbind(multiply, THREE), mapply(neighbors, neighbors(
        ORIGIN))))), shift(mapply(lbind(shift, merge(objects(I, T, T, T))),
        apply(rbind(multiply, THREE), mapply(neighbors, neighbors(ORIGIN)))
        ), UP_RIGHT)), shift(mapply(lbind(shift, merge(objects(I, T, T, T))
        ), apply(rbind(multiply, THREE), mapply(neighbors, neighbors(ORIGIN
        )))), DOWN_LEFT))


def solve_95990924(I):
    return fill(fill(fill(fill(I, ONE, apply(ulcorner, apply(outbox,
        objects(I, T, F, T)))), TWO, apply(urcorner, apply(outbox, objects(
        I, T, F, T)))), THREE, apply(llcorner, apply(outbox, objects(I, T,
        F, T)))), FOUR, apply(lrcorner, apply(outbox, objects(I, T, F, T))))


def solve_e509e548(I):
    return fill(fill(replace(I, THREE, SIX), TWO, mfilter(objects(I, T, F,
        T), compose(lbind(contained, THREE), chain(palette, trim, rbind(
        subgrid, I))))), ONE, mfilter(objects(I, T, F, T), fork(equality,
        size, compose(decrement, fork(add, height, width)))))


def solve_d43fd935(I):
    return paint(I, mapply(fork(recolor, color, fork(connect, center, fork(
        add, center, rbind(gravitate, ofcolor(I, THREE))))), sfilter(
        sizefilter(objects(I, T, F, T), ONE), fork(either, rbind(vmatching,
        ofcolor(I, THREE)), rbind(hmatching, ofcolor(I, THREE))))))


def solve_db3e9e38(I):
    return fill(fill(I, EIGHT, mapply(rbind(shoot, UP), combine(shoot(
        lrcorner(ofcolor(I, SEVEN)), UP_RIGHT), shoot(lrcorner(ofcolor(I,
        SEVEN)), NEG_UNITY)))), SEVEN, sfilter(mapply(rbind(shoot, UP),
        combine(shoot(lrcorner(ofcolor(I, SEVEN)), UP_RIGHT), shoot(
        lrcorner(ofcolor(I, SEVEN)), NEG_UNITY))), chain(even, rbind(
        subtract, last(lrcorner(ofcolor(I, SEVEN)))), last)))


def solve_e73095fd(I):
    return fill(I, FOUR, mfilter(sfilter(colorfilter(objects(I, T, F, F),
        ZERO), fork(equality, toindices, backdrop)), chain(matcher(size,
        ZERO), rbind(intersection, ofcolor(I, FIVE)), fork(difference,
        chain(lbind(mapply, dneighbors), corners, outbox), outbox))))


def solve_1bfc4729(I):
    return vconcat(fill(tophalf(I), leastcolor(tophalf(I)), combine(
        hfrontier(TWO_BY_ZERO), box(asindices(I)))), replace(hmirror(fill(
        tophalf(I), leastcolor(tophalf(I)), combine(hfrontier(TWO_BY_ZERO),
        box(asindices(I))))), leastcolor(tophalf(I)), leastcolor(bottomhalf
        (I))))


def solve_93b581b8(I):
    return fill(underpaint(I, shift(upscale(apply_func(chain(cmirror,
        dmirror, merge), fgpartition(I)), THREE), astuple(NEG_TWO, NEG_TWO)
        )), ZERO, difference(mapply(fork(combine, hfrontier, vfrontier),
        toindices(apply_func(chain(cmirror, dmirror, merge), fgpartition(I)
        ))), toindices(apply_func(chain(cmirror, dmirror, merge),
        fgpartition(I)))))


def solve_9edfc990(I):
    return paint(I, recolor(ONE, mfilter(colorfilter(objects(I, T, F, F),
        ZERO), rbind(adjacent, ofcolor(I, ONE)))))


def solve_a65b410d(I):
    return underfill(underfill(underfill(underfill(I, THREE, shoot(urcorner
        (ofcolor(I, TWO)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(I, TWO)),
        DOWN_LEFT)), ONE, mapply(rbind(shoot, LEFT), shoot(urcorner(ofcolor
        (I, TWO)), DOWN_LEFT))), THREE, mapply(rbind(shoot, LEFT), shoot(
        urcorner(ofcolor(I, TWO)), UP_RIGHT)))


def solve_7447852a(I):
    return fill(I, FOUR, mapply(first, sfilter(pair(order(colorfilter(
        objects(I, T, F, F), ZERO), compose(last, center)), interval(ZERO,
        size(order(colorfilter(objects(I, T, F, F), ZERO), compose(last,
        center))), ONE)), compose(rbind(contained, interval(ZERO, size(
        order(colorfilter(objects(I, T, F, F), ZERO), compose(last, center)
        )), THREE)), last))))


def solve_97999447(I):
    return fill(paint(I, mapply(fork(recolor, color, compose(rbind(shoot,
        RIGHT), center)), objects(I, T, F, T))), FIVE, merge(prapply(shift,
        apply(toindices, objects(I, T, F, T)), apply(tojvec, apply(
        increment, apply(double, interval(ZERO, FIVE, ONE)))))))


def solve_91714a58(I):
    return fill(paint(canvas(ZERO, shape(I)), argmax(objects(I, T, F, T),
        size)), ZERO, sfilter(asindices(I), compose(lbind(greater, THREE),
        chain(rbind(colorcount, mostcolor(argmax(objects(I, T, F, T), size)
        )), rbind(toobject, paint(canvas(ZERO, shape(I)), argmax(objects(I,
        T, F, T), size))), neighbors))))


def solve_a61ba2ce(I):
    return vconcat(hconcat(apply_func(chain(rbind(subgrid, I), lbind(
        extract, objects(I, T, F, T)), lbind(compose, matcher(lbind(index,
        I), ZERO))), lrcorner), apply_func(chain(rbind(subgrid, I), lbind(
        extract, objects(I, T, F, T)), lbind(compose, matcher(lbind(index,
        I), ZERO))), llcorner)), hconcat(apply_func(chain(rbind(subgrid, I),
        lbind(extract, objects(I, T, F, T)), lbind(compose, matcher(lbind(
        index, I), ZERO))), urcorner), apply_func(chain(rbind(subgrid, I),
        lbind(extract, objects(I, T, F, T)), lbind(compose, matcher(lbind(
        index, I), ZERO))), ulcorner)))


def solve_8e1813be(I):
    return apply_func(branch(vline(first(objects(replace(I, FIVE, ZERO), T,
        T, T))), dmirror, identity), apply(rbind(repeat, size(dedupe(apply(
        color, order(objects(apply_func(branch(vline(first(objects(replace(
        I, FIVE, ZERO), T, T, T))), dmirror, identity), replace(I, FIVE,
        ZERO)), T, T, T), uppermost))))), dedupe(apply(color, order(objects
        (apply_func(branch(vline(first(objects(replace(I, FIVE, ZERO), T, T,
        T))), dmirror, identity), replace(I, FIVE, ZERO)), T, T, T),
        uppermost)))))


def solve_bc1d5164(I):
    return fill(canvas(ZERO, THREE_BY_THREE), leastcolor(I), mapply(rbind(
        ofcolor, leastcolor(I)), combine(astuple(crop(I, ORIGIN,
        THREE_BY_THREE), crop(I, TWO_BY_ZERO, THREE_BY_THREE)), astuple(
        crop(I, tojvec(FOUR), THREE_BY_THREE), crop(I, astuple(TWO, FOUR),
        THREE_BY_THREE)))))


def solve_ce602527(I):
    return vmirror(subgrid(argmax(remove(last(order(fgpartition(vmirror(I)),
        size)), order(fgpartition(vmirror(I)), size)), chain(size, rbind(
        intersection, apply_func(compose(toindices, normalize), last(order(
        fgpartition(vmirror(I)), size)))), chain(toindices, rbind(upscale,
        TWO), normalize))), vmirror(I)))


def solve_5c2c9af4(I):
    return fill(I, leastcolor(I), shift(mapply(box, pair(apply(lbind(
        multiply, subtract(center(ofcolor(I, leastcolor(I))), ulcorner(
        ofcolor(I, leastcolor(I))))), interval(ZERO, NINE, ONE)), apply(
        lbind(multiply, subtract(center(ofcolor(I, leastcolor(I))),
        ulcorner(ofcolor(I, leastcolor(I))))), interval(ZERO, multiply(
        NEG_ONE, NINE), NEG_ONE)))), center(ofcolor(I, leastcolor(I)))))


def solve_75b8110e(I):
    return paint(paint(paint(tophalf(lefthalf(I)), apply_func(fork(toobject,
        fork(difference, asindices, rbind(ofcolor, ZERO)), identity),
        bottomhalf(righthalf(I)))), apply_func(fork(toobject, fork(
        difference, asindices, rbind(ofcolor, ZERO)), identity), bottomhalf
        (lefthalf(I)))), apply_func(fork(toobject, fork(difference,
        asindices, rbind(ofcolor, ZERO)), identity), tophalf(righthalf(I))))


def solve_941d9a10(I):
    return fill(fill(fill(I, ONE, apply_func(compose(lbind(extract, apply(
        toindices, colorfilter(objects(I, T, F, F), ZERO))), lbind(lbind,
        contained)), ORIGIN)), THREE, apply_func(compose(lbind(extract,
        apply(toindices, colorfilter(objects(I, T, F, F), ZERO))), lbind(
        lbind, contained)), decrement(shape(I)))), TWO, apply_func(compose(
        lbind(extract, apply(toindices, colorfilter(objects(I, T, F, F),
        ZERO))), lbind(lbind, contained)), astuple(FIVE, FIVE)))


def solve_c3f564a4(I):
    return paint(apply(lbind(apply, maximum), papply(pair, I, dmirror(I))),
        mapply(lbind(shift, toobject(difference(asindices(I), ofcolor(apply
        (lbind(apply, maximum), papply(pair, I, dmirror(I))), ZERO)), apply
        (lbind(apply, maximum), papply(pair, I, dmirror(I))))), pair(
        interval(invert(NINE), NINE, ONE), interval(NINE, invert(NINE),
        NEG_ONE))))


def solve_1a07d186(I):
    return paint(cover(I, merge(sizefilter(objects(I, T, F, T), ONE))),
        mapply(fork(shift, identity, fork(gravitate, identity, chain(first,
        lbind(colorfilter, difference(objects(I, T, F, T), sizefilter(
        objects(I, T, F, T), ONE))), color))), sfilter(sizefilter(objects(I,
        T, F, T), ONE), compose(rbind(contained, apply(color, difference(
        objects(I, T, F, T), sizefilter(objects(I, T, F, T), ONE)))), color))))


def solve_d687bc17(I):
    return paint(cover(I, merge(sizefilter(objects(I, T, F, T), ONE))),
        mapply(fork(shift, identity, fork(gravitate, identity, chain(first,
        lbind(colorfilter, difference(objects(I, T, F, T), sizefilter(
        objects(I, T, F, T), ONE))), color))), sfilter(sizefilter(objects(I,
        T, F, T), ONE), compose(rbind(contained, apply(color, difference(
        objects(I, T, F, T), sizefilter(objects(I, T, F, T), ONE)))), color))))


def solve_9af7a82c(I):
    return cmirror(merge(apply(compose(cmirror, fork(vconcat, fork(canvas,
        color, compose(rbind(astuple, ONE), size)), compose(lbind(canvas,
        ZERO), chain(rbind(astuple, ONE), lbind(subtract, valmax(objects(I,
        T, F, F), size)), size)))), order(objects(I, T, F, F), size))))


def solve_6e19193c(I):
    return fill(fill(I, leastcolor(I), mapply(fork(shoot, compose(first,
        delta), fork(subtract, compose(first, delta), chain(first, rbind(
        sfilter, chain(matcher(rbind(colorcount, leastcolor(I)), TWO),
        rbind(toobject, I), dneighbors)), toindices))), objects(I, T, F, T)
        )), ZERO, mapply(delta, objects(I, T, F, T)))


def solve_ef135b50(I):
    return paint(I, shift(asobject(trim(fill(I, NINE, intersection(mapply(
        fork(connect, first, last), sfilter(product(ofcolor(I, TWO),
        ofcolor(I, TWO)), fork(equality, power(first, TWO), compose(first,
        last)))), ofcolor(I, ZERO))))), UNITY))


def solve_cbded52d(I):
    return paint(I, mapply(fork(recolor, compose(color, first), chain(
        initset, center, fork(connect, compose(center, first), compose(
        center, last)))), sfilter(product(sizefilter(objects(I, T, F, T),
        ONE), sizefilter(objects(I, T, F, T), ONE)), fork(either, fork(
        vmatching, first, last), fork(hmatching, first, last)))))


def solve_8a004b2b(I):
    return paint(subgrid(ofcolor(I, FOUR), I), shift(upscale(normalize(
        argmax(objects(I, F, T, T), lowermost)), divide(width(merge(objects
        (replace(subgrid(ofcolor(I, FOUR), I), FOUR, ZERO), T, F, T))),
        width(argmax(objects(I, F, T, T), lowermost)))), ulcorner(merge(
        objects(replace(subgrid(ofcolor(I, FOUR), I), FOUR, ZERO), T, F, T)))))


def solve_e26a3af2(I):
    return apply_func(branch(greater(apply_func(compose(size, dedupe),
        apply(mostcommon, rot90(I))), apply_func(compose(size, dedupe),
        apply(mostcommon, I))), vupscale, hupscale), branch(greater(
        apply_func(compose(size, dedupe), apply(mostcommon, rot90(I))),
        apply_func(compose(size, dedupe), apply(mostcommon, I))), repeat(
        apply(mostcommon, rot90(I)), ONE), rot90(repeat(apply(mostcommon, I
        ), ONE))), apply_func(branch(greater(apply_func(compose(size,
        dedupe), apply(mostcommon, rot90(I))), apply_func(compose(size,
        dedupe), apply(mostcommon, I))), height, width), I))


def solve_6cf79266(I):
    return fill(I, ONE, mapply(lbind(shift, toindices(upscale(initset(
        astuple(ZERO, ORIGIN)), THREE))), sfilter(ofcolor(I, ZERO), fork(
        both, matcher(chain(size, rbind(difference, ofcolor(I, ZERO)),
        lbind(shift, toindices(upscale(initset(astuple(ZERO, ORIGIN)),
        THREE)))), ZERO), chain(flip, matcher(chain(size, rbind(difference,
        ofcolor(I, ZERO)), lbind(shift, toindices(upscale(initset(astuple(
        ZERO, ORIGIN)), THREE)))), ZERO), lbind(add, NEG_UNITY))))))


def solve_a87f7484(I):
    return apply_func(branch(portrait(I), dmirror, identity), extract(
        hsplit(apply_func(branch(portrait(I), dmirror, identity), I),
        decrement(numcolors(I))), matcher(rbind(ofcolor, ZERO), leastcommon
        (apply(rbind(ofcolor, ZERO), hsplit(apply_func(branch(portrait(I),
        dmirror, identity), I), decrement(numcolors(I))))))))


def solve_4093f84a(I):
    return apply_func(branch(portrait(ofcolor(I, FIVE)), identity, dmirror),
        hconcat(apply(rbind(order, identity), lefthalf(apply_func(branch(
        portrait(ofcolor(I, FIVE)), identity, dmirror), replace(I,
        leastcolor(I), FIVE)))), apply(rbind(order, invert), righthalf(
        apply_func(branch(portrait(ofcolor(I, FIVE)), identity, dmirror),
        replace(I, leastcolor(I), FIVE))))))


def solve_ba26e723(I):
    return fill(I, SIX, sfilter(ofcolor(I, FOUR), compose(fork(equality,
        identity, compose(rbind(multiply, THREE), rbind(divide, THREE))),
        last)))


def solve_4612dd53(I):
    return underfill(I, TWO, shift(ofcolor(fill(subgrid(ofcolor(I, ONE),
        fill(I, TWO, box(ofcolor(I, ONE)))), TWO, branch(greater(size(
        mapply(vfrontier, ofcolor(subgrid(ofcolor(I, ONE), fill(I, TWO, box
        (ofcolor(I, ONE)))), ONE))), size(mapply(hfrontier, ofcolor(subgrid
        (ofcolor(I, ONE), fill(I, TWO, box(ofcolor(I, ONE)))), ONE)))),
        mapply(hfrontier, ofcolor(subgrid(ofcolor(I, ONE), fill(I, TWO, box
        (ofcolor(I, ONE)))), ONE)), mapply(vfrontier, ofcolor(subgrid(
        ofcolor(I, ONE), fill(I, TWO, box(ofcolor(I, ONE)))), ONE)))), TWO),
        ulcorner(ofcolor(I, ONE))))


def solve_29c11459(I):
    return fill(paint(paint(I, mapply(fork(recolor, color, compose(
        hfrontier, center)), objects(righthalf(I), T, F, T))), merge(
        objects(paint(lefthalf(I), mapply(fork(recolor, color, compose(
        hfrontier, center)), objects(lefthalf(I), T, F, T))), T, F, T))),
        FIVE, shift(apply(urcorner, objects(paint(lefthalf(I), mapply(fork(
        recolor, color, compose(hfrontier, center)), objects(lefthalf(I), T,
        F, T))), T, F, T)), RIGHT))


def solve_963e52fc(I):
    return crop(rot270(merge(repeat(rot90(crop(I, ulcorner(asobject(I)),
        astuple(height(asobject(I)), hperiod(asobject(I))))), increment(
        divide(double(width(I)), hperiod(asobject(I))))))), ORIGIN, astuple
        (height(asobject(I)), double(width(I))))


def solve_ae3edfdc(I):
    return paint(paint(replace(replace(I, THREE, ZERO), SEVEN, ZERO),
        mapply(fork(shift, identity, apply_func(chain(lbind(rbind,
        gravitate), first, lbind(colorfilter, objects(I, T, F, T))), TWO)),
        apply_func(lbind(colorfilter, objects(I, T, F, T)), THREE))),
        mapply(fork(shift, identity, apply_func(chain(lbind(rbind,
        gravitate), first, lbind(colorfilter, objects(I, T, F, T))), ONE)),
        apply_func(lbind(colorfilter, objects(I, T, F, T)), SEVEN)))


def solve_1f0c79e5(I):
    return paint(I, mapply(lbind(shift, recolor(leastcolor(replace(I, TWO,
        ZERO)), combine(ofcolor(I, TWO), ofcolor(replace(I, TWO, ZERO),
        leastcolor(replace(I, TWO, ZERO)))))), prapply(multiply, apply(
        compose(decrement, double), shift(ofcolor(I, TWO), invert(ulcorner(
        combine(ofcolor(I, TWO), ofcolor(replace(I, TWO, ZERO), leastcolor(
        replace(I, TWO, ZERO)))))))), interval(ZERO, NINE, ONE))))


def solve_56dc2b01(I):
    return move(paint(I, shift(recolor(EIGHT, ofcolor(I, TWO)), crement(
        multiply(sign(gravitate(ofcolor(I, TWO), first(colorfilter(objects(
        I, T, F, T), THREE)))), apply_func(branch(equality(first(gravitate(
        first(colorfilter(objects(I, T, F, T), THREE)), ofcolor(I, TWO))),
        ZERO), width, height), first(colorfilter(objects(I, T, F, T), THREE
        ))))))), first(colorfilter(objects(I, T, F, T), THREE)), gravitate(
        first(colorfilter(objects(I, T, F, T), THREE)), ofcolor(I, TWO)))


def solve_e48d4e1a(I):
    return fill(canvas(ZERO, shape(I)), leastcolor(fill(I, ZERO, ofcolor(I,
        FIVE))), apply_func(fork(combine, vfrontier, hfrontier), add(
        multiply(DOWN_LEFT, size(ofcolor(I, FIVE))), extract(ofcolor(I,
        leastcolor(fill(I, ZERO, ofcolor(I, FIVE)))), matcher(chain(rbind(
        colorcount, leastcolor(fill(I, ZERO, ofcolor(I, FIVE)))), rbind(
        toobject, I), dneighbors), FOUR)))))


def solve_6773b310(I):
    return downscale(replace(fill(compress(I), ONE, mfilter(apply(rbind(
        toobject, compress(I)), apply(fork(insert, identity, neighbors),
        shift(apply(rbind(multiply, THREE), insert(ORIGIN, neighbors(ORIGIN
        ))), astuple(FOUR, FOUR)))), matcher(rbind(colorcount, SIX), TWO))),
        SIX, ZERO), THREE)


def solve_780d0b14(I):
    return rot270(sfilter(rot90(sfilter(paint(fill(I, ZERO, asindices(I)),
        pair(apply(color, totuple(sfilter(objects(I, T, T, T), compose(
        rbind(greater, TWO), size)))), apply(center, totuple(sfilter(
        objects(I, T, T, T), compose(rbind(greater, TWO), size)))))), chain
        (rbind(greater, ONE), size, compose(dedupe, totuple)))), chain(
        rbind(greater, ONE), size, compose(dedupe, totuple))))


def solve_2204b7a8(I):
    return apply_func(branch(greater(apply_func(compose(size, lbind(sfilter,
        objects(I, T, F, T))), vline), apply_func(compose(size, lbind(
        sfilter, objects(I, T, F, T))), hline)), hconcat, vconcat), replace
        (apply_func(branch(greater(apply_func(compose(size, lbind(sfilter,
        objects(I, T, F, T))), vline), apply_func(compose(size, lbind(
        sfilter, objects(I, T, F, T))), hline)), lefthalf, tophalf), I),
        THREE, index(apply_func(branch(greater(apply_func(compose(size,
        lbind(sfilter, objects(I, T, F, T))), vline), apply_func(compose(
        size, lbind(sfilter, objects(I, T, F, T))), hline)), lefthalf,
        tophalf), I), ORIGIN)), replace(apply_func(branch(greater(
        apply_func(compose(size, lbind(sfilter, objects(I, T, F, T))),
        vline), apply_func(compose(size, lbind(sfilter, objects(I, T, F, T)
        )), hline)), righthalf, bottomhalf), I), THREE, index(apply_func(
        branch(greater(apply_func(compose(size, lbind(sfilter, objects(I, T,
        F, T))), vline), apply_func(compose(size, lbind(sfilter, objects(I,
        T, F, T))), hline)), righthalf, bottomhalf), I), decrement(shape(
        apply_func(branch(greater(apply_func(compose(size, lbind(sfilter,
        objects(I, T, F, T))), vline), apply_func(compose(size, lbind(
        sfilter, objects(I, T, F, T))), hline)), righthalf, bottomhalf), I)))))
        )


def solve_d9f24cd1(I):
    return fill(fill(underfill(I, TWO, mfilter(prapply(connect, ofcolor(I,
        TWO), ofcolor(I, FIVE)), vline)), TWO, mapply(rbind(shoot, UP),
        shift(apply(urcorner, sfilter(objects(underfill(I, TWO, mfilter(
        prapply(connect, ofcolor(I, TWO), ofcolor(I, FIVE)), vline)), F, F,
        T), matcher(numcolors, TWO))), UNITY))), TWO, mapply(vfrontier,
        mapply(toindices, colorfilter(difference(objects(underfill(I, TWO,
        mfilter(prapply(connect, ofcolor(I, TWO), ofcolor(I, FIVE)), vline)
        ), F, F, T), sfilter(objects(underfill(I, TWO, mfilter(prapply(
        connect, ofcolor(I, TWO), ofcolor(I, FIVE)), vline)), F, F, T),
        matcher(numcolors, TWO))), TWO))))


def solve_b782dc8a(I):
    return fill(fill(I, leastcolor(I), sfilter(toindices(mfilter(
        colorfilter(objects(I, T, F, F), ZERO), rbind(adjacent, ofcolor(I,
        mostcolor(toobject(dneighbors(first(ofcolor(I, leastcolor(I)))), I)
        ))))), chain(even, rbind(manhattan, ofcolor(I, leastcolor(I))),
        initset))), mostcolor(toobject(dneighbors(first(ofcolor(I,
        leastcolor(I)))), I)), difference(toindices(mfilter(colorfilter(
        objects(I, T, F, F), ZERO), rbind(adjacent, ofcolor(I, mostcolor(
        toobject(dneighbors(first(ofcolor(I, leastcolor(I)))), I)))))),
        sfilter(toindices(mfilter(colorfilter(objects(I, T, F, F), ZERO),
        rbind(adjacent, ofcolor(I, mostcolor(toobject(dneighbors(first(
        ofcolor(I, leastcolor(I)))), I)))))), chain(even, rbind(manhattan,
        ofcolor(I, leastcolor(I))), initset))))


def solve_673ef223(I):
    return underfill(underfill(replace(I, EIGHT, FOUR), EIGHT, mapply(rbind
        (shoot, branch(equality(leftmost(argmin(objects(I, T, F, T),
        uppermost)), ZERO), LEFT, RIGHT)), ofcolor(I, EIGHT))), EIGHT,
        mapply(hfrontier, shift(ofcolor(I, EIGHT), toivec(apply_func(fork(
        subtract, maximum, minimum), apply(uppermost, colorfilter(objects(I,
        T, F, T), TWO)))))))


def solve_f5b8619d(I):
    return vconcat(hconcat(underfill(I, EIGHT, mapply(vfrontier, ofcolor(I,
        leastcolor(I)))), underfill(I, EIGHT, mapply(vfrontier, ofcolor(I,
        leastcolor(I))))), hconcat(underfill(I, EIGHT, mapply(vfrontier,
        ofcolor(I, leastcolor(I)))), underfill(I, EIGHT, mapply(vfrontier,
        ofcolor(I, leastcolor(I))))))


def solve_f8c80d96(I):
    return replace(fill(fill(fill(I, leastcolor(I), apply_func(chain(outbox,
        outbox, branch(equality(size(argmin(objects(I, T, F, F), width)),
        ONE), identity, outbox)), argmax(colorfilter(objects(I, T, F, F),
        leastcolor(I)), size))), leastcolor(I), apply_func(power(chain(
        outbox, outbox, branch(equality(size(argmin(objects(I, T, F, F),
        width)), ONE), identity, outbox)), TWO), argmax(colorfilter(objects
        (I, T, F, F), leastcolor(I)), size))), leastcolor(I), apply_func(
        power(chain(outbox, outbox, branch(equality(size(argmin(objects(I,
        T, F, F), width)), ONE), identity, outbox)), THREE), argmax(
        colorfilter(objects(I, T, F, F), leastcolor(I)), size))), ZERO, FIVE)


def solve_ecdecbb3(I):
    return fill(fill(I, TWO, mfilter(apply(fork(connect, compose(center,
        first), fork(add, compose(center, first), compose(crement, fork(
        gravitate, first, last)))), product(colorfilter(objects(I, T, F, T),
        TWO), colorfilter(objects(I, T, F, T), EIGHT))), compose(lbind(
        greater, EIGHT), size))), EIGHT, mapply(neighbors, intersection(
        mfilter(apply(fork(connect, compose(center, first), fork(add,
        compose(center, first), compose(crement, fork(gravitate, first,
        last)))), product(colorfilter(objects(I, T, F, T), TWO),
        colorfilter(objects(I, T, F, T), EIGHT))), compose(lbind(greater,
        EIGHT), size)), apply(fork(add, compose(center, first), compose(
        crement, fork(gravitate, first, last))), product(colorfilter(
        objects(I, T, F, T), TWO), colorfilter(objects(I, T, F, T), EIGHT))))))


def solve_e5062a87(I):
    return paint(I, recolor(TWO, merge(sfilter(apply(lbind(shift, normalize
        (recolor(ZERO, ofcolor(I, TWO)))), occurrences(I, recolor(ZERO,
        ofcolor(I, TWO)))), chain(flip, rbind(contained, insert(astuple(TWO,
        SIX), insert(astuple(FIVE, ONE), initset(astuple(ONE, THREE))))),
        ulcorner)))))


def solve_a8d7556c(I):
    return paint(fill(I, TWO, mapply(lbind(shift, upscale(recolor(ZERO,
        initset(ORIGIN)), TWO)), occurrences(I, upscale(recolor(ZERO,
        initset(ORIGIN)), TWO)))), branch(equality(index(fill(I, TWO,
        mapply(lbind(shift, upscale(recolor(ZERO, initset(ORIGIN)), TWO)),
        occurrences(I, upscale(recolor(ZERO, initset(ORIGIN)), TWO)))),
        astuple(EIGHT, add(SIX, SIX))), TWO), toobject(insert(add(astuple(
        EIGHT, add(SIX, SIX)), DOWN), initset(astuple(EIGHT, add(SIX, SIX))
        )), I), toobject(insert(add(astuple(EIGHT, add(SIX, SIX)), DOWN),
        initset(astuple(EIGHT, add(SIX, SIX)))), fill(I, TWO, mapply(lbind(
        shift, upscale(recolor(ZERO, initset(ORIGIN)), TWO)), occurrences(I,
        upscale(recolor(ZERO, initset(ORIGIN)), TWO)))))))


def solve_4938f0c2(I):
    return branch(greater(size(objects(I, T, T, T)), FOUR), I, fill(fill(I,
        TWO, shift(vmirror(ofcolor(I, TWO)), add(tojvec(width(ofcolor(I,
        TWO))), ZERO_BY_TWO))), TWO, shift(hmirror(ofcolor(fill(I, TWO,
        shift(vmirror(ofcolor(I, TWO)), add(tojvec(width(ofcolor(I, TWO))),
        ZERO_BY_TWO))), TWO)), add(toivec(height(ofcolor(I, TWO))),
        TWO_BY_ZERO))))


def solve_834ec97d(I):
    return fill(paint(fill(I, ZERO, first(objects(I, T, F, T))), shift(
        first(objects(I, T, F, T)), DOWN)), FOUR, sfilter(sfilter(asindices
        (I), compose(lbind(greater, uppermost(shift(first(objects(I, T, F,
        T)), DOWN))), first)), compose(rbind(contained, interval(subtract(
        leftmost(shift(first(objects(I, T, F, T)), DOWN)), TEN), add(
        leftmost(shift(first(objects(I, T, F, T)), DOWN)), TEN), TWO)), last)))


def solve_846bdb03(I):
    return paint(subgrid(merge(remove(extract(objects(I, F, F, T), matcher(
        rbind(colorcount, FOUR), ZERO)), objects(I, F, F, T))), I), shift(
        normalize(apply_func(branch(equality(index(subgrid(merge(remove(
        extract(objects(I, F, F, T), matcher(rbind(colorcount, FOUR), ZERO)
        ), objects(I, F, F, T))), I), DOWN), other(palette(lefthalf(subgrid
        (extract(objects(I, F, F, T), matcher(rbind(colorcount, FOUR), ZERO
        )), I))), ZERO)), identity, vmirror), extract(objects(I, F, F, T),
        matcher(rbind(colorcount, FOUR), ZERO)))), UNITY))


def solve_90f3ed37(I):
    return underfill(I, ONE, mapply(fork(argmax, chain(rbind(apply, apply(
        tojvec, interval(TWO, NEG_ONE, NEG_ONE))), lbind(lbind, shift),
        compose(lbind(shift, normalize(first(order(objects(I, T, T, T),
        uppermost)))), ulcorner)), compose(lbind(compose, size), lbind(
        lbind, intersection))), remove(first(order(objects(I, T, T, T),
        uppermost)), order(objects(I, T, T, T), uppermost))))


def solve_8403a5d5(I):
    return fill(fill(fill(I, color(first(objects(I, T, F, T))), sfilter(
        asindices(I), compose(rbind(contained, interval(leftmost(first(
        objects(I, T, F, T))), TEN, TWO)), last))), FIVE, apply(tojvec,
        interval(increment(leftmost(first(objects(I, T, F, T)))), TEN, FOUR
        ))), FIVE, apply(lbind(astuple, NINE), interval(add(leftmost(first(
        objects(I, T, F, T))), THREE), TEN, FOUR)))


def solve_91413438(I):
    return merge(hsplit(paint(hconcat(I, canvas(ZERO, astuple(THREE,
        subtract(multiply(multiply(colorcount(I, ZERO), THREE), colorcount(
        I, ZERO)), THREE)))), mapply(compose(lbind(shift, first(objects(
        hconcat(I, canvas(ZERO, astuple(THREE, subtract(multiply(multiply(
        colorcount(I, ZERO), THREE), colorcount(I, ZERO)), THREE)))), T, T,
        T))), tojvec), apply(rbind(multiply, THREE), interval(ZERO,
        subtract(NINE, colorcount(I, ZERO)), ONE)))), colorcount(I, ZERO)))


def solve_539a4f51(I):
    return paint(canvas(index(I, ORIGIN), multiply(UNITY, TEN)), asobject(
        vconcat(hconcat(crop(I, ORIGIN, branch(positive(colorcount(I, ZERO)
        ), decrement(shape(I)), shape(I))), vupscale(crop(crop(I, ORIGIN,
        branch(positive(colorcount(I, ZERO)), decrement(shape(I)), shape(I)
        )), ORIGIN, astuple(ONE, width(crop(I, ORIGIN, branch(positive(
        colorcount(I, ZERO)), decrement(shape(I)), shape(I)))))), width(
        crop(I, ORIGIN, branch(positive(colorcount(I, ZERO)), decrement(
        shape(I)), shape(I)))))), hconcat(dmirror(vupscale(crop(crop(I,
        ORIGIN, branch(positive(colorcount(I, ZERO)), decrement(shape(I)),
        shape(I))), ORIGIN, astuple(ONE, width(crop(I, ORIGIN, branch(
        positive(colorcount(I, ZERO)), decrement(shape(I)), shape(I)))))),
        width(crop(I, ORIGIN, branch(positive(colorcount(I, ZERO)),
        decrement(shape(I)), shape(I)))))), crop(I, ORIGIN, branch(positive
        (colorcount(I, ZERO)), decrement(shape(I)), shape(I)))))))


def solve_5daaa586(I):
    return fill(subgrid(outbox(extract(colorfilter(objects(I, T, F, F),
        ZERO), compose(flip, rbind(bordering, I)))), I), color(argmax(
        fgpartition(subgrid(outbox(extract(colorfilter(objects(I, T, F, F),
        ZERO), compose(flip, rbind(bordering, I)))), I)), size)), branch(
        greater(size(mfilter(prapply(connect, toindices(argmax(fgpartition(
        subgrid(outbox(extract(colorfilter(objects(I, T, F, F), ZERO),
        compose(flip, rbind(bordering, I)))), I)), size)), toindices(argmax
        (fgpartition(subgrid(outbox(extract(colorfilter(objects(I, T, F, F),
        ZERO), compose(flip, rbind(bordering, I)))), I)), size))), vline)),
        size(mfilter(prapply(connect, toindices(argmax(fgpartition(subgrid(
        outbox(extract(colorfilter(objects(I, T, F, F), ZERO), compose(flip,
        rbind(bordering, I)))), I)), size)), toindices(argmax(fgpartition(
        subgrid(outbox(extract(colorfilter(objects(I, T, F, F), ZERO),
        compose(flip, rbind(bordering, I)))), I)), size))), hline))),
        mfilter(prapply(connect, toindices(argmax(fgpartition(subgrid(
        outbox(extract(colorfilter(objects(I, T, F, F), ZERO), compose(flip,
        rbind(bordering, I)))), I)), size)), toindices(argmax(fgpartition(
        subgrid(outbox(extract(colorfilter(objects(I, T, F, F), ZERO),
        compose(flip, rbind(bordering, I)))), I)), size))), vline), mfilter
        (prapply(connect, toindices(argmax(fgpartition(subgrid(outbox(
        extract(colorfilter(objects(I, T, F, F), ZERO), compose(flip, rbind
        (bordering, I)))), I)), size)), toindices(argmax(fgpartition(
        subgrid(outbox(extract(colorfilter(objects(I, T, F, F), ZERO),
        compose(flip, rbind(bordering, I)))), I)), size))), hline)))


def solve_3bdb4ada(I):
    return fill(I, ZERO, mapply(fork(sfilter, first, compose(lbind(compose,
        compose(even, fork(subtract, compose(last, first), power(last, TWO)
        ))), lbind(rbind, astuple))), pair(papply(connect, apply(compose(
        increment, ulcorner), totuple(objects(I, T, F, T))), apply(compose(
        decrement, lrcorner), totuple(objects(I, T, F, T)))), apply(last,
        apply(compose(increment, ulcorner), totuple(objects(I, T, F, T)))))))


def solve_ec883f72(I):
    return underfill(I, other(remove(ZERO, palette(I)), color(argmax(
        objects(I, T, T, T), fork(multiply, height, width)))), combine(
        combine(shoot(lrcorner(argmax(objects(I, T, T, T), fork(multiply,
        height, width))), UNITY), shoot(llcorner(argmax(objects(I, T, T, T),
        fork(multiply, height, width))), DOWN_LEFT)), combine(shoot(
        urcorner(argmax(objects(I, T, T, T), fork(multiply, height, width))
        ), UP_RIGHT), shoot(ulcorner(argmax(objects(I, T, T, T), fork(
        multiply, height, width))), NEG_UNITY))))


def solve_2bee17df(I):
    return underfill(I, THREE, merge(astuple(mapply(hfrontier, sfilter(pair
        (interval(ZERO, height(I), ONE), apply_func(compose(lbind(apply,
        matcher(rbind(colorcount, ZERO), subtract(height(I), TWO))), rbind(
        vsplit, height(I))), I)), last)), mapply(vfrontier, sfilter(pair(
        apply_func(compose(lbind(apply, matcher(rbind(colorcount, ZERO),
        subtract(height(I), TWO))), rbind(vsplit, height(I))), rot90(I)),
        interval(ZERO, height(I), ONE)), first)))))


def solve_e8dc4411(I):
    return fill(I, leastcolor(I), mapply(lbind(shift, ofcolor(I, ZERO)),
        apply(lbind(multiply, apply(branch(equality(apply_func(fork(connect,
        ulcorner, lrcorner), ofcolor(I, ZERO)), intersection(ofcolor(I,
        ZERO), apply_func(fork(connect, ulcorner, lrcorner), ofcolor(I,
        ZERO)))), identity, fork(add, identity, fork(subtract, identity,
        crement))), multiply(shape(ofcolor(I, ZERO)), position(ofcolor(I,
        ZERO), ofcolor(I, leastcolor(I)))))), interval(ONE, FIVE, ONE))))


def solve_e40b9e2f(I):
    return paint(paint(I, argmax(apply(lbind(shift, apply_func(compose(
        hmirror, vmirror), first(objects(I, F, T, T)))), mapply(neighbors,
        neighbors(ORIGIN))), lbind(intersection, first(objects(I, F, T, T))
        ))), argmax(apply(lbind(shift, apply_func(compose(vmirror, dmirror),
        first(objects(paint(I, argmax(apply(lbind(shift, apply_func(compose
        (hmirror, vmirror), first(objects(I, F, T, T)))), mapply(neighbors,
        neighbors(ORIGIN))), lbind(intersection, first(objects(I, F, T, T))
        ))), F, T, T)))), mapply(neighbors, neighbors(ORIGIN))), compose(
        size, lbind(intersection, first(objects(I, F, T, T))))))


def solve_29623171(I):
    return fill(fill(I, leastcolor(I), mfilter(apply(fork(product, compose(
        fork(rbind(interval, ONE), identity, rbind(add, THREE)), first),
        compose(fork(rbind(interval, ONE), identity, rbind(add, THREE)),
        last)), product(interval(ZERO, NINE, FOUR), interval(ZERO, NINE,
        FOUR))), matcher(compose(rbind(colorcount, leastcolor(I)), rbind(
        toobject, I)), valmax(apply(fork(product, compose(fork(rbind(
        interval, ONE), identity, rbind(add, THREE)), first), compose(fork(
        rbind(interval, ONE), identity, rbind(add, THREE)), last)), product
        (interval(ZERO, NINE, FOUR), interval(ZERO, NINE, FOUR))), compose(
        rbind(colorcount, leastcolor(I)), rbind(toobject, I)))))), ZERO,
        mfilter(apply(fork(product, compose(fork(rbind(interval, ONE),
        identity, rbind(add, THREE)), first), compose(fork(rbind(interval,
        ONE), identity, rbind(add, THREE)), last)), product(interval(ZERO,
        NINE, FOUR), interval(ZERO, NINE, FOUR))), compose(flip, matcher(
        compose(rbind(colorcount, leastcolor(I)), rbind(toobject, I)),
        valmax(apply(fork(product, compose(fork(rbind(interval, ONE),
        identity, rbind(add, THREE)), first), compose(fork(rbind(interval,
        ONE), identity, rbind(add, THREE)), last)), product(interval(ZERO,
        NINE, FOUR), interval(ZERO, NINE, FOUR))), compose(rbind(colorcount,
        leastcolor(I)), rbind(toobject, I)))))))


def solve_a2fd1cf0(I):
    return underfill(I, EIGHT, combine(connect(astuple(minimum(astuple(
        uppermost(ofcolor(I, TWO)), uppermost(ofcolor(I, THREE)))),
        leftmost(ofcolor(I, THREE))), astuple(maximum(astuple(uppermost(
        ofcolor(I, TWO)), uppermost(ofcolor(I, THREE)))), leftmost(ofcolor(
        I, THREE)))), connect(astuple(uppermost(ofcolor(I, TWO)), minimum(
        astuple(leftmost(ofcolor(I, TWO)), leftmost(ofcolor(I, THREE))))),
        astuple(uppermost(ofcolor(I, TWO)), maximum(astuple(leftmost(
        ofcolor(I, TWO)), leftmost(ofcolor(I, THREE))))))))


def solve_b0c4d837(I):
    return vconcat(vconcat(first(hsplit(hconcat(canvas(EIGHT, astuple(ONE,
        subtract(decrement(height(ofcolor(I, FIVE))), height(ofcolor(I,
        EIGHT))))), canvas(ZERO, astuple(ONE, subtract(SIX, subtract(
        decrement(height(ofcolor(I, FIVE))), height(ofcolor(I, EIGHT))))))),
        TWO)), vmirror(last(hsplit(hconcat(canvas(EIGHT, astuple(ONE,
        subtract(decrement(height(ofcolor(I, FIVE))), height(ofcolor(I,
        EIGHT))))), canvas(ZERO, astuple(ONE, subtract(SIX, subtract(
        decrement(height(ofcolor(I, FIVE))), height(ofcolor(I, EIGHT))))))),
        TWO)))), canvas(ZERO, astuple(ONE, THREE)))


def solve_8731374e(I):
    return fill(rot270(merge(sfilter(vsplit(rot90(merge(sfilter(vsplit(
        subgrid(argmax(objects(I, T, F, F), size), I), height(subgrid(
        argmax(objects(I, T, F, F), size), I))), compose(lbind(greater,
        FOUR), numcolors)))), width(subgrid(argmax(objects(I, T, F, F),
        size), I))), compose(lbind(greater, FOUR), numcolors)))),
        leastcolor(rot270(merge(sfilter(vsplit(rot90(merge(sfilter(vsplit(
        subgrid(argmax(objects(I, T, F, F), size), I), height(subgrid(
        argmax(objects(I, T, F, F), size), I))), compose(lbind(greater,
        FOUR), numcolors)))), width(subgrid(argmax(objects(I, T, F, F),
        size), I))), compose(lbind(greater, FOUR), numcolors))))), mapply(
        fork(combine, vfrontier, hfrontier), ofcolor(rot270(merge(sfilter(
        vsplit(rot90(merge(sfilter(vsplit(subgrid(argmax(objects(I, T, F, F
        ), size), I), height(subgrid(argmax(objects(I, T, F, F), size), I))
        ), compose(lbind(greater, FOUR), numcolors)))), width(subgrid(
        argmax(objects(I, T, F, F), size), I))), compose(lbind(greater,
        FOUR), numcolors)))), leastcolor(rot270(merge(sfilter(vsplit(rot90(
        merge(sfilter(vsplit(subgrid(argmax(objects(I, T, F, F), size), I),
        height(subgrid(argmax(objects(I, T, F, F), size), I))), compose(
        lbind(greater, FOUR), numcolors)))), width(subgrid(argmax(objects(I,
        T, F, F), size), I))), compose(lbind(greater, FOUR), numcolors))))))))


def solve_272f95fa(I):
    return fill(fill(fill(fill(fill(I, SIX, extract(apply(toindices,
        colorfilter(objects(I, T, F, F), ZERO)), compose(flip, rbind(
        bordering, I)))), TWO, argmin(sfilter(remove(extract(apply(
        toindices, colorfilter(objects(I, T, F, F), ZERO)), compose(flip,
        rbind(bordering, I))), apply(toindices, colorfilter(objects(I, T, F,
        F), ZERO))), lbind(vmatching, extract(apply(toindices, colorfilter(
        objects(I, T, F, F), ZERO)), compose(flip, rbind(bordering, I))))),
        uppermost)), ONE, argmax(sfilter(remove(extract(apply(toindices,
        colorfilter(objects(I, T, F, F), ZERO)), compose(flip, rbind(
        bordering, I))), apply(toindices, colorfilter(objects(I, T, F, F),
        ZERO))), lbind(vmatching, extract(apply(toindices, colorfilter(
        objects(I, T, F, F), ZERO)), compose(flip, rbind(bordering, I))))),
        uppermost)), FOUR, argmin(sfilter(remove(extract(apply(toindices,
        colorfilter(objects(I, T, F, F), ZERO)), compose(flip, rbind(
        bordering, I))), apply(toindices, colorfilter(objects(I, T, F, F),
        ZERO))), lbind(hmatching, extract(apply(toindices, colorfilter(
        objects(I, T, F, F), ZERO)), compose(flip, rbind(bordering, I))))),
        leftmost)), THREE, argmax(sfilter(remove(extract(apply(toindices,
        colorfilter(objects(I, T, F, F), ZERO)), compose(flip, rbind(
        bordering, I))), apply(toindices, colorfilter(objects(I, T, F, F),
        ZERO))), lbind(hmatching, extract(apply(toindices, colorfilter(
        objects(I, T, F, F), ZERO)), compose(flip, rbind(bordering, I))))),
        leftmost))


def solve_db93a21d(I):
    return fill(fill(fill(underfill(I, ONE, mapply(rbind(shoot, DOWN),
        ofcolor(I, NINE))), THREE, mapply(outbox, colorfilter(objects(I, T,
        T, T), NINE))), THREE, mapply(power(outbox, TWO), sfilter(
        colorfilter(objects(I, T, T, T), NINE), compose(rbind(greater, ONE),
        compose(halve, width))))), THREE, mapply(power(outbox, THREE),
        sfilter(colorfilter(objects(I, T, T, T), NINE), matcher(compose(
        halve, width), THREE))))


def solve_53b68214(I):
    return paint(paint(canvas(ZERO, astuple(width(I), width(I))), first(
        objects(I, T, T, T))), branch(portrait(first(objects(I, T, T, T))),
        mapply(lbind(shift, first(objects(I, T, T, T))), apply(lbind(
        multiply, toivec(vperiod(first(objects(I, T, T, T))))), interval(
        ZERO, NINE, ONE))), shift(first(objects(I, T, T, T)), decrement(add
        (DOWN, shape(first(objects(I, T, T, T))))))))


def solve_d6ad076f(I):
    return cover(underfill(I, EIGHT, mapply(rbind(shoot, multiply(branch(
        vmatching(argmin(objects(I, T, F, T), size), argmax(objects(I, T, F,
        T), size)), DOWN, RIGHT), branch(equality(valmax(objects(I, T, F, T
        ), branch(vmatching(argmin(objects(I, T, F, T), size), argmax(
        objects(I, T, F, T), size)), uppermost, leftmost)), apply_func(
        branch(vmatching(argmin(objects(I, T, F, T), size), argmax(objects(
        I, T, F, T), size)), uppermost, leftmost), argmin(objects(I, T, F,
        T), size))), NEG_ONE, ONE))), inbox(argmin(objects(I, T, F, T),
        size)))), mfilter(colorfilter(objects(underfill(I, EIGHT, mapply(
        rbind(shoot, multiply(branch(vmatching(argmin(objects(I, T, F, T),
        size), argmax(objects(I, T, F, T), size)), DOWN, RIGHT), branch(
        equality(valmax(objects(I, T, F, T), branch(vmatching(argmin(
        objects(I, T, F, T), size), argmax(objects(I, T, F, T), size)),
        uppermost, leftmost)), apply_func(branch(vmatching(argmin(objects(I,
        T, F, T), size), argmax(objects(I, T, F, T), size)), uppermost,
        leftmost), argmin(objects(I, T, F, T), size))), NEG_ONE, ONE))),
        inbox(argmin(objects(I, T, F, T), size)))), T, F, T), EIGHT), rbind
        (bordering, I)))


def solve_6cdd2623(I):
    return fill(cover(I, merge(fgpartition(I))), leastcolor(I), mfilter(
        prapply(connect, ofcolor(I, leastcolor(I)), ofcolor(I, leastcolor(I
        ))), fork(both, fork(either, hline, vline), chain(positive, size,
        rbind(difference, box(merge(fgpartition(I))))))))


def solve_a3df8b1e(I):
    return hmirror(crop(hmirror(vconcat(vconcat(vconcat(crop(subgrid(first(
        objects(fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)),
        ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE
        )), UP_RIGHT)), ONE)), NEG_UNITY)), T, T, T)), fill(fill(I, ONE,
        shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(
        ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)
        ), NEG_UNITY))), DOWN, subtract(shape(subgrid(first(objects(fill(
        fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(
        urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE)),
        UP_RIGHT)), ONE)), NEG_UNITY)), T, T, T)), fill(fill(I, ONE, shoot(
        first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(
        fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)),
        NEG_UNITY)))), DOWN)), crop(subgrid(first(objects(fill(fill(I, ONE,
        shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(
        ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)
        ), NEG_UNITY)), T, T, T)), fill(fill(I, ONE, shoot(first(ofcolor(I,
        ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(
        first(ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY))), DOWN,
        subtract(shape(subgrid(first(objects(fill(fill(I, ONE, shoot(first(
        ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I,
        ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY)),
        T, T, T)), fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT
        )), ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I,
        ONE)), UP_RIGHT)), ONE)), NEG_UNITY)))), DOWN))), vconcat(crop(
        subgrid(first(objects(fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)
        ), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first
        (ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY)), T, T, T)), fill(
        fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(
        urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE)),
        UP_RIGHT)), ONE)), NEG_UNITY))), DOWN, subtract(shape(subgrid(first
        (objects(fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)),
        ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE
        )), UP_RIGHT)), ONE)), NEG_UNITY)), T, T, T)), fill(fill(I, ONE,
        shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(
        ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)
        ), NEG_UNITY)))), DOWN)), crop(subgrid(first(objects(fill(fill(I,
        ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(
        ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)
        ), NEG_UNITY)), T, T, T)), fill(fill(I, ONE, shoot(first(ofcolor(I,
        ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(
        first(ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY))), DOWN,
        subtract(shape(subgrid(first(objects(fill(fill(I, ONE, shoot(first(
        ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I,
        ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY)),
        T, T, T)), fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT
        )), ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I,
        ONE)), UP_RIGHT)), ONE)), NEG_UNITY)))), DOWN)))), vconcat(vconcat(
        crop(subgrid(first(objects(fill(fill(I, ONE, shoot(first(ofcolor(I,
        ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(
        first(ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY)), T, T, T)),
        fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE,
        shoot(urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE)),
        UP_RIGHT)), ONE)), NEG_UNITY))), DOWN, subtract(shape(subgrid(first
        (objects(fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)),
        ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE
        )), UP_RIGHT)), ONE)), NEG_UNITY)), T, T, T)), fill(fill(I, ONE,
        shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(
        ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)
        ), NEG_UNITY)))), DOWN)), crop(subgrid(first(objects(fill(fill(I,
        ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(
        ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)
        ), NEG_UNITY)), T, T, T)), fill(fill(I, ONE, shoot(first(ofcolor(I,
        ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(
        first(ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY))), DOWN,
        subtract(shape(subgrid(first(objects(fill(fill(I, ONE, shoot(first(
        ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I,
        ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY)),
        T, T, T)), fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT
        )), ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I,
        ONE)), UP_RIGHT)), ONE)), NEG_UNITY)))), DOWN))), vconcat(crop(
        subgrid(first(objects(fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)
        ), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first
        (ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY)), T, T, T)), fill(
        fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(
        urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE)),
        UP_RIGHT)), ONE)), NEG_UNITY))), DOWN, subtract(shape(subgrid(first
        (objects(fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)),
        ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE
        )), UP_RIGHT)), ONE)), NEG_UNITY)), T, T, T)), fill(fill(I, ONE,
        shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(
        ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)
        ), NEG_UNITY)))), DOWN)), crop(subgrid(first(objects(fill(fill(I,
        ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(
        ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)
        ), NEG_UNITY)), T, T, T)), fill(fill(I, ONE, shoot(first(ofcolor(I,
        ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(
        first(ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY))), DOWN,
        subtract(shape(subgrid(first(objects(fill(fill(I, ONE, shoot(first(
        ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I,
        ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY)),
        T, T, T)), fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT
        )), ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I,
        ONE)), UP_RIGHT)), ONE)), NEG_UNITY)))), DOWN)))))), ORIGIN, shape(I)))


def solve_8d510a79(I):
    return fill(underfill(I, TWO, mapply(fork(sfilter, fork(shoot, identity,
        compose(chain(toivec, decrement, double), compose(lbind(greater,
        uppermost(ofcolor(I, FIVE))), first))), compose(lbind(matcher,
        compose(lbind(greater, uppermost(ofcolor(I, FIVE))), first)),
        compose(lbind(greater, uppermost(ofcolor(I, FIVE))), first))),
        ofcolor(I, TWO))), ONE, mapply(fork(shoot, identity, chain(invert,
        chain(toivec, decrement, double), compose(lbind(greater, uppermost(
        ofcolor(I, FIVE))), first))), ofcolor(I, ONE)))


def solve_cdecee7f(I):
    return vconcat(vconcat(crop(merge(hsplit(hconcat(dmirror(merge(apply(
        rbind(canvas, UNITY), apply(color, order(objects(I, T, F, T),
        leftmost))))), canvas(ZERO, astuple(ONE, subtract(NINE, size(
        objects(I, T, F, T)))))), THREE)), ORIGIN, astuple(ONE, THREE)),
        vmirror(crop(merge(hsplit(hconcat(dmirror(merge(apply(rbind(canvas,
        UNITY), apply(color, order(objects(I, T, F, T), leftmost))))),
        canvas(ZERO, astuple(ONE, subtract(NINE, size(objects(I, T, F, T)))
        ))), THREE)), DOWN, astuple(ONE, THREE)))), crop(merge(hsplit(
        hconcat(dmirror(merge(apply(rbind(canvas, UNITY), apply(color,
        order(objects(I, T, F, T), leftmost))))), canvas(ZERO, astuple(ONE,
        subtract(NINE, size(objects(I, T, F, T)))))), THREE)), TWO_BY_ZERO,
        astuple(ONE, THREE)))


def solve_3345333e(I):
    return fill(cover(I, ofcolor(I, leastcolor(I))), leastcolor(cover(I,
        ofcolor(I, leastcolor(I)))), argmax(apply(lbind(shift, vmirror(
        ofcolor(cover(I, ofcolor(I, leastcolor(I))), leastcolor(cover(I,
        ofcolor(I, leastcolor(I))))))), mapply(neighbors, neighbors(ORIGIN)
        )), compose(size, rbind(intersection, ofcolor(cover(I, ofcolor(I,
        leastcolor(I))), leastcolor(cover(I, ofcolor(I, leastcolor(I)))))))))


def solve_b190f7f5(I):
    return fill(upscale(argmax(apply_func(branch(portrait(I), vsplit,
        hsplit), I, TWO), numcolors), width(argmax(apply_func(branch(
        portrait(I), vsplit, hsplit), I, TWO), numcolors))), ZERO, ofcolor(
        apply_func(chain(dmirror, merge, rbind(repeat, width(argmax(
        apply_func(branch(portrait(I), vsplit, hsplit), I, TWO), numcolors)
        ))), apply_func(chain(dmirror, merge, rbind(repeat, width(argmax(
        apply_func(branch(portrait(I), vsplit, hsplit), I, TWO), numcolors)
        ))), argmin(apply_func(branch(portrait(I), vsplit, hsplit), I, TWO),
        numcolors))), ZERO))


def solve_caa06a1f(I):
    return paint(I, mapply(lbind(shift, shift(first(objects(paint(canvas(
        index(I, decrement(shape(I))), double(shape(I))), asobject(I)), F,
        F, T)), LEFT)), apply(lbind(multiply, astuple(vperiod(shift(first(
        objects(paint(canvas(index(I, decrement(shape(I))), double(shape(I)
        )), asobject(I)), F, F, T)), LEFT)), hperiod(shift(first(objects(
        paint(canvas(index(I, decrement(shape(I))), double(shape(I))),
        asobject(I)), F, F, T)), LEFT)))), apply_func(power(lbind(mapply,
        neighbors), TWO), neighbors(ORIGIN)))))


def solve_e21d9049(I):
    return cover(paint(I, mapply(lbind(shift, merge(objects(I, T, F, T))),
        apply(lbind(multiply, shape(merge(objects(I, T, F, T)))),
        apply_func(power(lbind(mapply, neighbors), TWO), neighbors(ORIGIN))
        ))), difference(asindices(I), sfilter(asindices(I), compose(fork(
        either, lbind(hmatching, ofcolor(I, leastcolor(I))), lbind(
        vmatching, ofcolor(I, leastcolor(I)))), initset))))


def solve_d89b689b(I):
    return paint(cover(I, merge(sizefilter(objects(I, T, F, T), ONE))),
        mapply(fork(recolor, color, compose(lbind(argmin, apply(initset,
        ofcolor(I, EIGHT))), lbind(rbind, manhattan))), sizefilter(objects(
        I, T, F, T), ONE)))


def solve_746b3537(I):
    return apply_func(branch(equality(apply_func(chain(size, dedupe, first),
        I), ONE), dmirror, identity), repeat(apply(color, order(objects(
        apply_func(branch(equality(apply_func(chain(size, dedupe, first), I
        ), ONE), dmirror, identity), I), T, F, F), leftmost)), ONE))


def solve_63613498(I):
    return paint(fill(I, FIVE, mfilter(objects(I, T, F, T), matcher(compose
        (toindices, normalize), normalize(difference(asindices(crop(I,
        ORIGIN, THREE_BY_THREE)), ofcolor(crop(I, ORIGIN, THREE_BY_THREE),
        ZERO)))))), asobject(crop(I, ORIGIN, THREE_BY_THREE)))


def solve_06df4c85(I):
    return fill(paint(I, mfilter(apply(fork(recolor, color, fork(connect,
        compose(last, first), power(last, TWO))), sfilter(product(merge(
        remove(argmax(partition(I), size), difference(partition(I),
        colorfilter(partition(I), ZERO)))), merge(remove(argmax(partition(I
        ), size), difference(partition(I), colorfilter(partition(I), ZERO))
        ))), fork(equality, power(first, TWO), compose(first, last)))),
        fork(either, vline, hline))), mostcolor(I), ofcolor(I, mostcolor(I)))


def solve_f9012d9b(I):
    return subgrid(ofcolor(I, ZERO), paint(I, mapply(lbind(shift, mfilter(
        objects(I, T, F, F), chain(flip, lbind(contained, ZERO), palette))),
        apply(rbind(multiply, astuple(vperiod(asobject(extract(vsplit(I,
        TWO), chain(flip, lbind(contained, ZERO), palette)))), hperiod(
        asobject(extract(hsplit(I, TWO), chain(flip, lbind(contained, ZERO),
        palette)))))), mapply(neighbors, neighbors(ORIGIN))))))


def solve_4522001f(I):
    return branch(contained(TWO_BY_ZERO, toindices(first(objects(I, F, F, T
        )))), rot270(paint(canvas(ZERO, astuple(NINE, NINE)), combine(
        upscale(upscale(initset(astuple(THREE, ORIGIN)), TWO), TWO), shift(
        upscale(upscale(initset(astuple(THREE, ORIGIN)), TWO), TWO), shape(
        upscale(upscale(initset(astuple(THREE, ORIGIN)), TWO), TWO)))))),
        branch(contained(TWO_BY_TWO, toindices(first(objects(I, F, F, T)))),
        rot180(paint(canvas(ZERO, astuple(NINE, NINE)), combine(upscale(
        upscale(initset(astuple(THREE, ORIGIN)), TWO), TWO), shift(upscale(
        upscale(initset(astuple(THREE, ORIGIN)), TWO), TWO), shape(upscale(
        upscale(initset(astuple(THREE, ORIGIN)), TWO), TWO)))))), branch(
        contained(ZERO_BY_TWO, toindices(first(objects(I, F, F, T)))),
        rot90(paint(canvas(ZERO, astuple(NINE, NINE)), combine(upscale(
        upscale(initset(astuple(THREE, ORIGIN)), TWO), TWO), shift(upscale(
        upscale(initset(astuple(THREE, ORIGIN)), TWO), TWO), shape(upscale(
        upscale(initset(astuple(THREE, ORIGIN)), TWO), TWO)))))), paint(
        canvas(ZERO, astuple(NINE, NINE)), combine(upscale(upscale(initset(
        astuple(THREE, ORIGIN)), TWO), TWO), shift(upscale(upscale(initset(
        astuple(THREE, ORIGIN)), TWO), TWO), shape(upscale(upscale(initset(
        astuple(THREE, ORIGIN)), TWO), TWO))))))))


def solve_a48eeaf7(I):
    return fill(cover(I, ofcolor(I, FIVE)), FIVE, mapply(compose(lbind(
        argmin, apply(initset, outbox(ofcolor(I, TWO)))), compose(lbind(
        lbind, manhattan), initset)), ofcolor(I, FIVE)))


def solve_eb5a1d5d(I):
    return apply_func(fork(vconcat, identity, compose(hmirror, fork(remove,
        last, identity))), dmirror(apply_func(fork(vconcat, identity,
        compose(hmirror, fork(remove, last, identity))), apply_func(compose
        (dmirror, dedupe), apply_func(compose(dmirror, dedupe), I)))))


def solve_e179c5f4(I):
    return replace(hmirror(crop(merge(repeat(crop(fill(fill(I, ONE, shoot(
        first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(
        fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)),
        NEG_UNITY)), ulcorner(ofcolor(fill(fill(I, ONE, shoot(first(ofcolor
        (I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I, ONE,
        shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY)), ONE)),
        astuple(decrement(height(subgrid(ofcolor(fill(fill(I, ONE, shoot(
        first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(
        fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)),
        NEG_UNITY)), ONE), fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)),
        UP_RIGHT)), ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first(
        ofcolor(I, ONE)), UP_RIGHT)), ONE)), NEG_UNITY))))), width(subgrid(
        ofcolor(fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)),
        ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE
        )), UP_RIGHT)), ONE)), NEG_UNITY)), ONE), fill(fill(I, ONE, shoot(
        first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(
        fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)),
        NEG_UNITY)))))), NINE)), ORIGIN, astuple(height(I), width(subgrid(
        ofcolor(fill(fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)),
        ONE, shoot(urcorner(ofcolor(fill(I, ONE, shoot(first(ofcolor(I, ONE
        )), UP_RIGHT)), ONE)), NEG_UNITY)), ONE), fill(fill(I, ONE, shoot(
        first(ofcolor(I, ONE)), UP_RIGHT)), ONE, shoot(urcorner(ofcolor(
        fill(I, ONE, shoot(first(ofcolor(I, ONE)), UP_RIGHT)), ONE)),
        NEG_UNITY))))))), ZERO, EIGHT)


def solve_228f6490(I):
    return move(move(I, extract(difference(objects(I, T, F, F), colorfilter
        (objects(I, T, F, F), ZERO)), matcher(compose(normalize, toindices),
        apply_func(compose(normalize, toindices), first(sfilter(colorfilter
        (objects(I, T, F, F), ZERO), compose(flip, rbind(bordering, I))))))
        ), subtract(ulcorner(first(sfilter(colorfilter(objects(I, T, F, F),
        ZERO), compose(flip, rbind(bordering, I))))), ulcorner(extract(
        difference(objects(I, T, F, F), colorfilter(objects(I, T, F, F),
        ZERO)), matcher(compose(normalize, toindices), apply_func(compose(
        normalize, toindices), first(sfilter(colorfilter(objects(I, T, F, F
        ), ZERO), compose(flip, rbind(bordering, I)))))))))), extract(
        difference(objects(I, T, F, F), colorfilter(objects(I, T, F, F),
        ZERO)), matcher(compose(normalize, toindices), apply_func(compose(
        normalize, toindices), last(sfilter(colorfilter(objects(I, T, F, F),
        ZERO), compose(flip, rbind(bordering, I))))))), subtract(ulcorner(
        last(sfilter(colorfilter(objects(I, T, F, F), ZERO), compose(flip,
        rbind(bordering, I))))), ulcorner(extract(difference(objects(I, T,
        F, F), colorfilter(objects(I, T, F, F), ZERO)), matcher(compose(
        normalize, toindices), apply_func(compose(normalize, toindices),
        last(sfilter(colorfilter(objects(I, T, F, F), ZERO), compose(flip,
        rbind(bordering, I))))))))))


def solve_995c5fa3(I):
    return hupscale(merge(apply(compose(rbind(canvas, UNITY), fork(add,
        fork(add, compose(double, matcher(compose(size, rbind(ofcolor, ZERO
        )), ZERO)), chain(power(double, TWO), double, matcher(compose(
        ulcorner, rbind(ofcolor, ZERO)), UNITY))), fork(add, compose(rbind(
        multiply, THREE), matcher(compose(ulcorner, rbind(ofcolor, ZERO)),
        DOWN)), compose(power(double, TWO), matcher(compose(ulcorner, rbind
        (ofcolor, ZERO)), astuple(TWO, ONE)))))), hsplit(I, THREE))), THREE)


def solve_d06dbe63(I):
    return rot180(fill(rot180(fill(I, FIVE, mapply(lbind(shift, shift(
        combine(connect(ORIGIN, DOWN), connect(ORIGIN, ZERO_BY_TWO)),
        subtract(center(ofcolor(I, EIGHT)), TWO_BY_ZERO))), apply(lbind(
        multiply, astuple(NEG_TWO, TWO)), interval(ZERO, FIVE, ONE))))),
        FIVE, shift(shift(mapply(lbind(shift, shift(combine(connect(ORIGIN,
        DOWN), connect(ORIGIN, ZERO_BY_TWO)), subtract(center(ofcolor(I,
        EIGHT)), TWO_BY_ZERO))), apply(lbind(multiply, astuple(NEG_TWO, TWO
        )), interval(ZERO, FIVE, ONE))), subtract(center(ofcolor(rot180(
        fill(I, FIVE, mapply(lbind(shift, shift(combine(connect(ORIGIN,
        DOWN), connect(ORIGIN, ZERO_BY_TWO)), subtract(center(ofcolor(I,
        EIGHT)), TWO_BY_ZERO))), apply(lbind(multiply, astuple(NEG_TWO, TWO
        )), interval(ZERO, FIVE, ONE))))), EIGHT)), subtract(center(ofcolor
        (I, EIGHT)), TWO_BY_ZERO))), toivec(NEG_TWO))))


def solve_36fdfd69(I):
    return downscale(paint(fill(upscale(I, TWO), FOUR, mapply(delta, apply(
        merge, sfilter(product(colorfilter(objects(upscale(I, TWO), T, T, T
        ), TWO), colorfilter(objects(upscale(I, TWO), T, T, T), TWO)),
        compose(lbind(greater, FIVE), fork(manhattan, first, last)))))),
        merge(colorfilter(objects(upscale(I, TWO), T, T, T), TWO))), TWO)


def solve_0a938d79(I):
    return apply_func(branch(portrait(I), dmirror, identity), paint(
        apply_func(branch(portrait(I), dmirror, identity), I), mapply(fork(
        recolor, color, chain(lbind(mapply, compose(vfrontier, tojvec)),
        rbind(rbind(interval, apply_func(chain(double, decrement, width),
        merge(fgpartition(apply_func(branch(portrait(I), dmirror, identity),
        I))))), width(apply_func(branch(portrait(I), dmirror, identity), I)
        )), leftmost)), fgpartition(apply_func(branch(portrait(I), dmirror,
        identity), I)))))


def solve_045e512c(I):
    return paint(I, mapply(fork(recolor, color, compose(lbind(mapply, lbind
        (shift, argmax(objects(I, T, T, T), size))), chain(rbind(apply,
        interval(FOUR, double(TEN), FOUR)), lbind(rbind, multiply), lbind(
        position, argmax(objects(I, T, T, T), size))))), remove(argmax(
        objects(I, T, T, T), size), objects(I, T, T, T))))


def solve_82819916(I):
    return paint(I, mapply(fork(combine, fork(recolor, compose(first, rbind
        (argmin, compose(last, last))), compose(lbind(shift, sfilter(
        normalize(argmax(objects(I, F, T, T), size)), matcher(first,
        apply_func(compose(first, rbind(argmin, compose(last, last))),
        normalize(argmax(objects(I, F, T, T), size)))))), compose(toivec,
        uppermost))), fork(recolor, fork(other, palette, compose(first,
        rbind(argmin, compose(last, last)))), compose(lbind(shift,
        difference(normalize(argmax(objects(I, F, T, T), size)), sfilter(
        normalize(argmax(objects(I, F, T, T), size)), matcher(first,
        apply_func(compose(first, rbind(argmin, compose(last, last))),
        normalize(argmax(objects(I, F, T, T), size))))))), compose(toivec,
        uppermost)))), remove(argmax(objects(I, F, T, T), size), objects(I,
        F, T, T))))


def solve_99fa7670(I):
    return underpaint(paint(I, mapply(fork(recolor, color, compose(rbind(
        shoot, RIGHT), center)), objects(I, T, F, T))), mapply(fork(recolor,
        compose(color, first), fork(connect, compose(lrcorner, first),
        compose(lrcorner, last))), pair(remove(recolor(ZERO, initset(add(
        shape(I), DOWN_LEFT))), order(insert(recolor(ZERO, initset(add(
        shape(I), DOWN_LEFT))), objects(paint(I, mapply(fork(recolor, color,
        compose(rbind(shoot, RIGHT), center)), objects(I, T, F, T))), T, F,
        T)), uppermost)), remove(first(order(insert(recolor(ZERO, initset(
        add(shape(I), DOWN_LEFT))), objects(paint(I, mapply(fork(recolor,
        color, compose(rbind(shoot, RIGHT), center)), objects(I, T, F, T))),
        T, F, T)), uppermost)), order(insert(recolor(ZERO, initset(add(
        shape(I), DOWN_LEFT))), objects(paint(I, mapply(fork(recolor, color,
        compose(rbind(shoot, RIGHT), center)), objects(I, T, F, T))), T, F,
        T)), uppermost)))))


def solve_72322fa7(I):
    return paint(paint(I, mapply(fork(mapply, compose(lbind(lbind, shift),
        normalize), compose(lbind(occurrences, I), fork(sfilter, identity,
        compose(lbind(matcher, first), mostcolor)))), difference(objects(I,
        F, T, T), sfilter(objects(I, F, T, T), matcher(numcolors, ONE))))),
        mapply(fork(mapply, compose(lbind(lbind, shift), normalize), fork(
        apply, compose(lbind(rbind, add), fork(subtract, ulcorner, compose(
        ulcorner, fork(difference, identity, fork(sfilter, identity,
        compose(lbind(matcher, first), mostcolor)))))), compose(lbind(
        occurrences, I), fork(difference, identity, fork(sfilter, identity,
        compose(lbind(matcher, first), mostcolor)))))), difference(objects(
        I, F, T, T), sfilter(objects(I, F, T, T), matcher(numcolors, ONE)))))


def solve_855e0971(I):
    return apply_func(branch(positive(size(sfilter(frontiers(I), hline))),
        identity, dmirror), fill(apply_func(branch(positive(size(sfilter(
        frontiers(I), hline))), identity, dmirror), I), ZERO, mapply(fork(
        intersection, toindices, fork(shift, chain(lbind(mapply, vfrontier),
        rbind(ofcolor, ZERO), rbind(subgrid, apply_func(branch(positive(
        size(sfilter(frontiers(I), hline))), identity, dmirror), I))),
        ulcorner)), sfilter(partition(apply_func(branch(positive(size(
        sfilter(frontiers(I), hline))), identity, dmirror), I)), compose(
        flip, matcher(color, ZERO))))))


def solve_a78176bb(I):
    return replace(fill(I, other(remove(ZERO, palette(I)), FIVE), combine(
        mapply(fork(combine, rbind(shoot, UNITY), rbind(shoot, NEG_UNITY)),
        apply(rbind(add, UP_RIGHT), apply(urcorner, sfilter(colorfilter(
        objects(I, T, F, T), FIVE), matcher(compose(lbind(index, I),
        urcorner), FIVE))))), mapply(fork(combine, rbind(shoot, UNITY),
        rbind(shoot, NEG_UNITY)), apply(rbind(add, DOWN_LEFT), apply(
        llcorner, difference(colorfilter(objects(I, T, F, T), FIVE),
        sfilter(colorfilter(objects(I, T, F, T), FIVE), matcher(compose(
        lbind(index, I), urcorner), FIVE)))))))), FIVE, ZERO)


def solve_952a094c(I):
    return paint(cover(I, merge(sizefilter(objects(I, T, F, T), ONE))),
        apply(fork(astuple, compose(color, chain(lbind(argmax, sizefilter(
        objects(I, T, F, T), ONE)), lbind(rbind, manhattan), initset)),
        identity), corners(outbox(argmax(objects(I, T, F, T), size)))))


def solve_6d58a25d(I):
    return underfill(I, color(merge(remove(argmax(objects(I, T, T, T), size
        ), objects(I, T, T, T)))), mapply(chain(rbind(sfilter, compose(
        rbind(greater, increment(uppermost(argmax(objects(I, T, T, T), size
        )))), first)), vfrontier, center), sfilter(remove(argmax(objects(I,
        T, T, T), size), objects(I, T, T, T)), fork(both, rbind(vmatching,
        argmax(objects(I, T, T, T), size)), compose(rbind(greater,
        uppermost(argmax(objects(I, T, T, T), size))), uppermost)))))


def solve_6aa20dc0(I):
    return paint(I, mapply(fork(mapply, lbind(lbind, shift), compose(lbind(
        occurrences, I), fork(difference, identity, fork(sfilter, identity,
        compose(lbind(matcher, first), mostcolor))))), rapply(apply(fork(
        compose, first, last), product(insert(dmirror, insert(cmirror,
        insert(hmirror, insert(vmirror, initset(identity))))), apply(lbind(
        rbind, upscale), interval(ONE, FOUR, ONE)))), normalize(argmax(
        objects(I, F, T, T), numcolors)))))


def solve_e6721834(I):
    return paint(first(order(apply_func(branch(portrait(I), vsplit, hsplit),
        I, TWO), numcolors)), mfilter(apply(fork(shift, identity, fork(
        subtract, chain(first, lbind(occurrences, first(order(apply_func(
        branch(portrait(I), vsplit, hsplit), I, TWO), numcolors))), rbind(
        sfilter, compose(flip, matcher(first, mostcolor(merge(objects(last(
        order(apply_func(branch(portrait(I), vsplit, hsplit), I, TWO),
        numcolors)), F, F, T))))))), compose(ulcorner, rbind(sfilter,
        compose(flip, matcher(first, mostcolor(merge(objects(last(order(
        apply_func(branch(portrait(I), vsplit, hsplit), I, TWO), numcolors)
        ), F, F, T))))))))), sfilter(objects(last(order(apply_func(branch(
        portrait(I), vsplit, hsplit), I, TWO), numcolors)), F, F, T), chain
        (positive, size, compose(lbind(occurrences, first(order(apply_func(
        branch(portrait(I), vsplit, hsplit), I, TWO), numcolors))), rbind(
        sfilter, compose(flip, matcher(first, mostcolor(merge(objects(last(
        order(apply_func(branch(portrait(I), vsplit, hsplit), I, TWO),
        numcolors)), F, F, T)))))))))), chain(positive, decrement, compose(
        decrement, width))))


def solve_447fd412(I):
    return paint(I, mapply(fork(mapply, lbind(lbind, shift), compose(lbind(
        apply, increment), fork(apply, chain(lbind(rbind, subtract),
        ulcorner, fork(difference, identity, fork(sfilter, identity,
        compose(lbind(matcher, first), mostcolor)))), chain(lbind(
        occurrences, I), fork(combine, identity, compose(lbind(recolor,
        ZERO), outbox)), fork(difference, identity, fork(sfilter, identity,
        compose(lbind(matcher, first), mostcolor))))))), rapply(apply(lbind
        (rbind, upscale), interval(ONE, FOUR, ONE)), normalize(argmax(
        objects(I, F, T, T), numcolors)))))


def solve_2bcee788(I):
    return paint(replace(I, mostcolor(I), THREE), shift(sfilter(asobject(
        branch(hline(argmin(objects(I, T, F, T), size)), hmirror(subgrid(
        argmax(objects(I, T, F, T), size), replace(I, mostcolor(I), THREE))
        ), vmirror(subgrid(argmax(objects(I, T, F, T), size), replace(I,
        mostcolor(I), THREE))))), compose(flip, matcher(first, THREE))),
        add(ulcorner(argmax(objects(I, T, F, T), size)), multiply(shape(
        argmax(objects(I, T, F, T), size)), astuple(branch(hline(argmin(
        objects(I, T, F, T), size)), first(position(argmax(objects(I, T, F,
        T), size), argmin(objects(I, T, F, T), size))), ZERO), branch(hline
        (argmin(objects(I, T, F, T), size)), ZERO, last(position(argmax(
        objects(I, T, F, T), size), argmin(objects(I, T, F, T), size)))))))))


def solve_776ffc46(I):
    return fill(I, color(normalize(sfilter(asobject(subgrid(inbox(extract(
        colorfilter(objects(I, T, F, T), FIVE), fork(equality, toindices,
        box))), I)), compose(flip, matcher(first, ZERO))))), mfilter(
        objects(I, T, F, T), matcher(compose(toindices, normalize),
        toindices(normalize(sfilter(asobject(subgrid(inbox(extract(
        colorfilter(objects(I, T, F, T), FIVE), fork(equality, toindices,
        box))), I)), compose(flip, matcher(first, ZERO))))))))


def solve_f35d900a(I):
    return fill(paint(I, mapply(fork(recolor, compose(lbind(other, remove(
        ZERO, palette(I))), color), outbox), objects(I, T, F, T))), FIVE,
        sfilter(difference(box(mapply(toindices, objects(I, T, F, T))),
        mapply(toindices, objects(I, T, F, T))), compose(even, fork(
        manhattan, initset, chain(initset, lbind(argmin, mapply(toindices,
        objects(I, T, F, T))), chain(rbind(compose, initset), lbind(rbind,
        manhattan), initset))))))


def solve_0dfd9992(I):
    return paint(I, mapply(lbind(shift, merge(difference(partition(I),
        colorfilter(partition(I), ZERO)))), apply(lbind(multiply, astuple(
        vperiod(asobject(crop(I, tojvec(decrement(height(I))), astuple(
        height(I), ONE)))), hperiod(asobject(crop(I, toivec(decrement(width
        (I))), astuple(ONE, width(I))))))), mapply(neighbors, neighbors(
        ORIGIN)))))


def solve_29ec7d0e(I):
    return paint(I, mapply(lbind(shift, merge(difference(partition(I),
        colorfilter(partition(I), ZERO)))), apply(lbind(multiply, astuple(
        vperiod(asobject(crop(I, tojvec(decrement(height(I))), astuple(
        height(I), ONE)))), hperiod(asobject(crop(I, toivec(decrement(width
        (I))), astuple(ONE, width(I))))))), mapply(neighbors, neighbors(
        ORIGIN)))))


def solve_36d67576(I):
    return paint(I, mapply(fork(mapply, compose(lbind(lbind, shift),
        normalize), fork(apply, chain(compose(lbind(rbind, subtract),
        ulcorner), rbind(sfilter, compose(rbind(contained, astuple(TWO,
        FOUR)), first)), normalize), chain(lbind(occurrences, I), rbind(
        sfilter, compose(rbind(contained, astuple(TWO, FOUR)), first)),
        normalize))), rapply(combine(combine(astuple(cmirror, dmirror),
        astuple(hmirror, vmirror)), totuple(apply(fork(compose, first, last
        ), product(combine(astuple(cmirror, dmirror), astuple(hmirror,
        vmirror)), combine(astuple(cmirror, dmirror), astuple(hmirror,
        vmirror)))))), argmax(objects(I, F, F, T), numcolors))))


def solve_98cf29f8(I):
    return fill(cover(I, other(fgpartition(I), extract(fgpartition(I), fork
        (equality, size, fork(multiply, height, width))))), color(other(
        fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(
        multiply, height, width))))), shift(backdrop(outbox(sfilter(other(
        fgpartition(I), extract(fgpartition(I), fork(equality, size, fork(
        multiply, height, width)))), chain(rbind(greater, THREE), rbind(
        colorcount, color(other(fgpartition(I), extract(fgpartition(I),
        fork(equality, size, fork(multiply, height, width)))))), chain(
        rbind(toobject, I), ineighbors, last))))), gravitate(backdrop(
        outbox(sfilter(other(fgpartition(I), extract(fgpartition(I), fork(
        equality, size, fork(multiply, height, width)))), chain(rbind(
        greater, THREE), rbind(colorcount, color(other(fgpartition(I),
        extract(fgpartition(I), fork(equality, size, fork(multiply, height,
        width)))))), chain(rbind(toobject, I), ineighbors, last))))),
        extract(fgpartition(I), fork(equality, size, fork(multiply, height,
        width))))))


def solve_469497ad(I):
    return paint(underfill(upscale(I, decrement(numcolors(I))), TWO,
        combine(combine(shoot(ulcorner(argmin(objects(upscale(I, decrement(
        numcolors(I))), F, F, T), size)), NEG_UNITY), shoot(ulcorner(argmin
        (objects(upscale(I, decrement(numcolors(I))), F, F, T), size)),
        UNITY)), combine(shoot(llcorner(argmin(objects(upscale(I, decrement
        (numcolors(I))), F, F, T), size)), DOWN_LEFT), shoot(llcorner(
        argmin(objects(upscale(I, decrement(numcolors(I))), F, F, T), size)
        ), UP_RIGHT)))), argmax(objects(underfill(upscale(I, decrement(
        numcolors(I))), TWO, combine(combine(shoot(ulcorner(argmin(objects(
        upscale(I, decrement(numcolors(I))), F, F, T), size)), NEG_UNITY),
        shoot(ulcorner(argmin(objects(upscale(I, decrement(numcolors(I))),
        F, F, T), size)), UNITY)), combine(shoot(llcorner(argmin(objects(
        upscale(I, decrement(numcolors(I))), F, F, T), size)), DOWN_LEFT),
        shoot(llcorner(argmin(objects(upscale(I, decrement(numcolors(I))),
        F, F, T), size)), UP_RIGHT)))), T, F, T), lrcorner))


def solve_39e1d7f9(I):
    return paint(I, mapply(lbind(shift, asobject(crop(I, decrement(subtract
        (ulcorner(argmax(colorfilter(objects(I, T, F, T), color(last(remove
        (last(order(fgpartition(I), height)), order(fgpartition(I), height)
        )))), chain(numcolors, rbind(toobject, I), power(outbox, TWO)))),
        shape(argmax(colorfilter(objects(I, T, F, T), color(last(remove(
        last(order(fgpartition(I), height)), order(fgpartition(I), height))
        ))), chain(numcolors, rbind(toobject, I), power(outbox, TWO)))))),
        add(multiply(shape(argmax(colorfilter(objects(I, T, F, T), color(
        last(remove(last(order(fgpartition(I), height)), order(fgpartition(
        I), height))))), chain(numcolors, rbind(toobject, I), power(outbox,
        TWO)))), THREE), TWO_BY_TWO)))), apply(rbind(subtract, increment(
        shape(argmax(colorfilter(objects(I, T, F, T), color(last(remove(
        last(order(fgpartition(I), height)), order(fgpartition(I), height))
        ))), chain(numcolors, rbind(toobject, I), power(outbox, TWO)))))),
        apply(ulcorner, colorfilter(objects(I, T, F, T), color(last(remove(
        last(order(fgpartition(I), height)), order(fgpartition(I), height))
        )))))))


def solve_484b58aa(I):
    return paint(I, mapply(lbind(shift, merge(difference(partition(I),
        colorfilter(partition(I), ZERO)))), apply(lbind(multiply, astuple(
        vperiod(asobject(crop(I, tojvec(apply_func(power(decrement, TWO),
        height(I))), astuple(height(I), TWO)))), hperiod(asobject(crop(I,
        toivec(apply_func(power(decrement, TWO), width(I))), astuple(TWO,
        width(I))))))), mapply(neighbors, neighbors(ORIGIN)))))


def solve_3befdf3e(I):
    return fill(underfill(switch(I, leastcolor(I), other(remove(ZERO,
        palette(I)), leastcolor(I))), other(remove(ZERO, palette(I)),
        leastcolor(I)), mapply(compose(backdrop, compose(first, fork(rapply,
        chain(initset, first, lbind(rapply, initset(compose(lbind(power,
        outbox), compose(width, inbox))))), identity))), objects(I, F, F, T
        ))), ZERO, mapply(fork(intersection, compose(backdrop, compose(
        first, fork(rapply, chain(initset, first, lbind(rapply, initset(
        compose(lbind(power, outbox), compose(width, inbox))))), identity))
        ), fork(mapply, compose(lbind(lbind(chain, backdrop), inbox),
        compose(lbind(power, outbox), compose(width, inbox))), chain(lbind(
        apply, initset), corners, compose(backdrop, compose(first, fork(
        rapply, chain(initset, first, lbind(rapply, initset(compose(lbind(
        power, outbox), compose(width, inbox))))), identity)))))), objects(
        I, F, F, T)))


def solve_9aec4887(I):
    return fill(paint(subgrid(other(objects(I, F, T, T), argmin(objects(I,
        F, T, T), numcolors)), I), apply(fork(astuple, chain(first, lbind(
        argmin, normalize(other(objects(I, F, T, T), argmin(objects(I, F, T,
        T), numcolors)))), chain(rbind(compose, initset), lbind(rbind,
        manhattan), initset)), identity), toindices(shift(normalize(argmin(
        objects(I, F, T, T), numcolors)), UNITY)))), EIGHT, intersection(
        toindices(shift(normalize(argmin(objects(I, F, T, T), numcolors)),
        UNITY)), apply_func(fork(combine, identity, vmirror), apply_func(
        fork(connect, ulcorner, lrcorner), toindices(shift(normalize(argmin
        (objects(I, F, T, T), numcolors)), UNITY))))))


def solve_49d1d64f(I):
    return paint(paint(canvas(ZERO, add(shape(I), TWO)), shift(asobject(I),
        UNITY)), apply(fork(astuple, chain(first, lbind(argmin, shift(
        asobject(I), UNITY)), chain(rbind(compose, initset), lbind(lbind,
        manhattan), initset)), identity), apply_func(fork(difference, box,
        corners), asindices(canvas(ZERO, add(shape(I), TWO))))))


def solve_57aa92db(I):
    return paint(paint(I, mapply(fork(recolor, chain(chain(first, lbind(
        remove, ZERO), palette), rbind(toobject, I), outbox), fork(upscale,
        compose(lbind(shift, normalize(argmax(objects(I, F, T, T), fork(
        subtract, compose(maximum, fork(apply, lbind(lbind, colorcount),
        palette)), compose(minimum, fork(apply, lbind(lbind, colorcount),
        palette)))))), fork(subtract, ulcorner, compose(lbind(multiply,
        ulcorner(sfilter(normalize(argmax(objects(I, F, T, T), fork(
        subtract, compose(maximum, fork(apply, lbind(lbind, colorcount),
        palette)), compose(minimum, fork(apply, lbind(lbind, colorcount),
        palette))))), matcher(first, leastcolor(argmax(objects(I, F, T, T),
        fork(subtract, compose(maximum, fork(apply, lbind(lbind, colorcount
        ), palette)), compose(minimum, fork(apply, lbind(lbind, colorcount),
        palette))))))))), width))), width)), colorfilter(objects(I, T, F, T
        ), leastcolor(argmax(objects(I, F, T, T), fork(subtract, compose(
        maximum, fork(apply, lbind(lbind, colorcount), palette)), compose(
        minimum, fork(apply, lbind(lbind, colorcount), palette)))))))),
        merge(objects(I, T, F, T)))


def solve_aba27056(I):
    return fill(fill(fill(I, FOUR, delta(mapply(toindices, objects(I, T, F,
        T)))), FOUR, mapply(lbind(shift, difference(box(mapply(toindices,
        objects(I, T, F, T))), mapply(toindices, objects(I, T, F, T)))),
        apply(lbind(multiply, position(delta(mapply(toindices, objects(I, T,
        F, T))), difference(box(mapply(toindices, objects(I, T, F, T))),
        mapply(toindices, objects(I, T, F, T))))), interval(ZERO, NINE, ONE
        )))), FOUR, mapply(fork(shoot, first, fork(subtract, last, first)),
        product(corners(difference(box(mapply(toindices, objects(I, T, F, T
        ))), mapply(toindices, objects(I, T, F, T)))), sfilter(sfilter(
        ofcolor(fill(fill(I, FOUR, delta(mapply(toindices, objects(I, T, F,
        T)))), FOUR, mapply(lbind(shift, difference(box(mapply(toindices,
        objects(I, T, F, T))), mapply(toindices, objects(I, T, F, T)))),
        apply(lbind(multiply, position(delta(mapply(toindices, objects(I, T,
        F, T))), difference(box(mapply(toindices, objects(I, T, F, T))),
        mapply(toindices, objects(I, T, F, T))))), interval(ZERO, NINE, ONE
        )))), ZERO), matcher(chain(rbind(colorcount, ZERO), rbind(toobject,
        fill(fill(I, FOUR, delta(mapply(toindices, objects(I, T, F, T)))),
        FOUR, mapply(lbind(shift, difference(box(mapply(toindices, objects(
        I, T, F, T))), mapply(toindices, objects(I, T, F, T)))), apply(
        lbind(multiply, position(delta(mapply(toindices, objects(I, T, F, T
        ))), difference(box(mapply(toindices, objects(I, T, F, T))), mapply
        (toindices, objects(I, T, F, T))))), interval(ZERO, NINE, ONE))))),
        dneighbors), TWO)), compose(fork(both, rbind(adjacent, mapply(
        toindices, objects(I, T, F, T))), rbind(adjacent, mapply(lbind(
        shift, difference(box(mapply(toindices, objects(I, T, F, T))),
        mapply(toindices, objects(I, T, F, T)))), apply(lbind(multiply,
        position(delta(mapply(toindices, objects(I, T, F, T))), difference(
        box(mapply(toindices, objects(I, T, F, T))), mapply(toindices,
        objects(I, T, F, T))))), interval(ZERO, NINE, ONE))))), initset)))))


def solve_f1cefba8(I):
    return fill(fill(I, other(remove(ZERO, palette(I)), leastcolor(fill(
        subgrid(first(objects(I, F, F, T)), I), ZERO, shift(asindices(
        apply_func(power(trim, TWO), subgrid(first(objects(I, F, F, T)), I)
        )), TWO_BY_TWO)))), combine(mapply(vfrontier, sfilter(shift(ofcolor
        (fill(subgrid(first(objects(I, F, F, T)), I), ZERO, shift(asindices
        (apply_func(power(trim, TWO), subgrid(first(objects(I, F, F, T)), I
        ))), TWO_BY_TWO)), leastcolor(fill(subgrid(first(objects(I, F, F, T
        )), I), ZERO, shift(asindices(apply_func(power(trim, TWO), subgrid(
        first(objects(I, F, F, T)), I))), TWO_BY_TWO)))), ulcorner(first(
        objects(I, F, F, T)))), fork(either, matcher(first, uppermost(
        ofcolor(I, leastcolor(fill(subgrid(first(objects(I, F, F, T)), I),
        ZERO, shift(asindices(apply_func(power(trim, TWO), subgrid(first(
        objects(I, F, F, T)), I))), TWO_BY_TWO)))))), matcher(first,
        lowermost(ofcolor(I, leastcolor(fill(subgrid(first(objects(I, F, F,
        T)), I), ZERO, shift(asindices(apply_func(power(trim, TWO), subgrid
        (first(objects(I, F, F, T)), I))), TWO_BY_TWO))))))))), mapply(
        hfrontier, difference(shift(ofcolor(fill(subgrid(first(objects(I, F,
        F, T)), I), ZERO, shift(asindices(apply_func(power(trim, TWO),
        subgrid(first(objects(I, F, F, T)), I))), TWO_BY_TWO)), leastcolor(
        fill(subgrid(first(objects(I, F, F, T)), I), ZERO, shift(asindices(
        apply_func(power(trim, TWO), subgrid(first(objects(I, F, F, T)), I)
        )), TWO_BY_TWO)))), ulcorner(first(objects(I, F, F, T)))), sfilter(
        shift(ofcolor(fill(subgrid(first(objects(I, F, F, T)), I), ZERO,
        shift(asindices(apply_func(power(trim, TWO), subgrid(first(objects(
        I, F, F, T)), I))), TWO_BY_TWO)), leastcolor(fill(subgrid(first(
        objects(I, F, F, T)), I), ZERO, shift(asindices(apply_func(power(
        trim, TWO), subgrid(first(objects(I, F, F, T)), I))), TWO_BY_TWO)))
        ), ulcorner(first(objects(I, F, F, T)))), fork(either, matcher(
        first, uppermost(ofcolor(I, leastcolor(fill(subgrid(first(objects(I,
        F, F, T)), I), ZERO, shift(asindices(apply_func(power(trim, TWO),
        subgrid(first(objects(I, F, F, T)), I))), TWO_BY_TWO)))))), matcher
        (first, lowermost(ofcolor(I, leastcolor(fill(subgrid(first(objects(
        I, F, F, T)), I), ZERO, shift(asindices(apply_func(power(trim, TWO),
        subgrid(first(objects(I, F, F, T)), I))), TWO_BY_TWO)))))))))))),
        leastcolor(fill(subgrid(first(objects(I, F, F, T)), I), ZERO, shift
        (asindices(apply_func(power(trim, TWO), subgrid(first(objects(I, F,
        F, T)), I))), TWO_BY_TWO))), intersection(ofcolor(I, ZERO), combine
        (mapply(vfrontier, sfilter(shift(ofcolor(fill(subgrid(first(objects
        (I, F, F, T)), I), ZERO, shift(asindices(apply_func(power(trim, TWO
        ), subgrid(first(objects(I, F, F, T)), I))), TWO_BY_TWO)),
        leastcolor(fill(subgrid(first(objects(I, F, F, T)), I), ZERO, shift
        (asindices(apply_func(power(trim, TWO), subgrid(first(objects(I, F,
        F, T)), I))), TWO_BY_TWO)))), ulcorner(first(objects(I, F, F, T)))),
        fork(either, matcher(first, uppermost(ofcolor(I, leastcolor(fill(
        subgrid(first(objects(I, F, F, T)), I), ZERO, shift(asindices(
        apply_func(power(trim, TWO), subgrid(first(objects(I, F, F, T)), I)
        )), TWO_BY_TWO)))))), matcher(first, lowermost(ofcolor(I,
        leastcolor(fill(subgrid(first(objects(I, F, F, T)), I), ZERO, shift
        (asindices(apply_func(power(trim, TWO), subgrid(first(objects(I, F,
        F, T)), I))), TWO_BY_TWO))))))))), mapply(hfrontier, difference(
        shift(ofcolor(fill(subgrid(first(objects(I, F, F, T)), I), ZERO,
        shift(asindices(apply_func(power(trim, TWO), subgrid(first(objects(
        I, F, F, T)), I))), TWO_BY_TWO)), leastcolor(fill(subgrid(first(
        objects(I, F, F, T)), I), ZERO, shift(asindices(apply_func(power(
        trim, TWO), subgrid(first(objects(I, F, F, T)), I))), TWO_BY_TWO)))
        ), ulcorner(first(objects(I, F, F, T)))), sfilter(shift(ofcolor(
        fill(subgrid(first(objects(I, F, F, T)), I), ZERO, shift(asindices(
        apply_func(power(trim, TWO), subgrid(first(objects(I, F, F, T)), I)
        )), TWO_BY_TWO)), leastcolor(fill(subgrid(first(objects(I, F, F, T)
        ), I), ZERO, shift(asindices(apply_func(power(trim, TWO), subgrid(
        first(objects(I, F, F, T)), I))), TWO_BY_TWO)))), ulcorner(first(
        objects(I, F, F, T)))), fork(either, matcher(first, uppermost(
        ofcolor(I, leastcolor(fill(subgrid(first(objects(I, F, F, T)), I),
        ZERO, shift(asindices(apply_func(power(trim, TWO), subgrid(first(
        objects(I, F, F, T)), I))), TWO_BY_TWO)))))), matcher(first,
        lowermost(ofcolor(I, leastcolor(fill(subgrid(first(objects(I, F, F,
        T)), I), ZERO, shift(asindices(apply_func(power(trim, TWO), subgrid
        (first(objects(I, F, F, T)), I))), TWO_BY_TWO)))))))))))))


def solve_1e32b0e9(I):
    return underfill(I, first(difference(difference(palette(asobject(I)),
        palette(extract(partition(crop(I, ORIGIN, astuple(divide(subtract(
        height(I), TWO), THREE), divide(subtract(height(I), TWO), THREE)))),
        compose(flip, matcher(color, ZERO))))), initset(mostcolor(I)))),
        mapply(lbind(shift, extract(partition(crop(I, ORIGIN, astuple(
        divide(subtract(height(I), TWO), THREE), divide(subtract(height(I),
        TWO), THREE)))), compose(flip, matcher(color, ZERO)))), papply(
        astuple, papply(add, apply(lbind(multiply, divide(subtract(height(I
        ), TWO), THREE)), apply(first, totuple(product(interval(ZERO, THREE,
        ONE), interval(ZERO, THREE, ONE))))), apply(first, totuple(product(
        interval(ZERO, THREE, ONE), interval(ZERO, THREE, ONE))))), papply(
        add, apply(lbind(multiply, divide(subtract(height(I), TWO), THREE)),
        apply(last, totuple(product(interval(ZERO, THREE, ONE), interval(
        ZERO, THREE, ONE))))), apply(last, totuple(product(interval(ZERO,
        THREE, ONE), interval(ZERO, THREE, ONE))))))))


def solve_28e73c20(I):
    return apply_func(power(fork(vconcat, compose(lbind(hupscale, canvas(
        THREE, UNITY)), height), fork(vconcat, compose(rbind(hconcat,
        canvas(THREE, UNITY)), chain(lbind(hupscale, canvas(ZERO, UNITY)),
        decrement, height)), rot90)), subtract(width(I), FOUR)), branch(
        even(width(I)), fill(upscale(canvas(THREE, UNITY), FOUR), ZERO,
        insert(astuple(TWO, TWO), insert(astuple(ONE, TWO), insert(UNITY,
        initset(DOWN))))), fill(hupscale(vupscale(canvas(THREE, UNITY),
        FIVE), THREE), ZERO, insert(astuple(THREE, ONE), insert(astuple(TWO,
        ONE), insert(UNITY, initset(DOWN)))))))


def solve_4c5c2cf0(I):
    return paint(paint(I, shift(first(objects(hmirror(subgrid(first(objects
        (I, F, T, T)), I)), F, T, T)), subtract(center(extract(objects(I, T,
        T, T), compose(fork(equality, identity, rot90), rbind(subgrid, I)))
        ), center(extract(objects(hmirror(subgrid(first(objects(I, F, T, T)
        ), I)), T, T, T), compose(fork(equality, identity, rot90), rbind(
        subgrid, I))))))), shift(first(objects(vmirror(subgrid(first(
        objects(paint(I, shift(first(objects(hmirror(subgrid(first(objects(
        I, F, T, T)), I)), F, T, T)), subtract(center(extract(objects(I, T,
        T, T), compose(fork(equality, identity, rot90), rbind(subgrid, I)))
        ), center(extract(objects(hmirror(subgrid(first(objects(I, F, T, T)
        ), I)), T, T, T), compose(fork(equality, identity, rot90), rbind(
        subgrid, I))))))), F, T, T)), paint(I, shift(first(objects(hmirror(
        subgrid(first(objects(I, F, T, T)), I)), F, T, T)), subtract(center
        (extract(objects(I, T, T, T), compose(fork(equality, identity,
        rot90), rbind(subgrid, I)))), center(extract(objects(hmirror(
        subgrid(first(objects(I, F, T, T)), I)), T, T, T), compose(fork(
        equality, identity, rot90), rbind(subgrid, I))))))))), F, T, T)),
        subtract(center(extract(objects(I, T, T, T), compose(fork(equality,
        identity, rot90), rbind(subgrid, I)))), center(extract(objects(
        vmirror(subgrid(first(objects(paint(I, shift(first(objects(hmirror(
        subgrid(first(objects(I, F, T, T)), I)), F, T, T)), subtract(center
        (extract(objects(I, T, T, T), compose(fork(equality, identity,
        rot90), rbind(subgrid, I)))), center(extract(objects(hmirror(
        subgrid(first(objects(I, F, T, T)), I)), T, T, T), compose(fork(
        equality, identity, rot90), rbind(subgrid, I))))))), F, T, T)),
        paint(I, shift(first(objects(hmirror(subgrid(first(objects(I, F, T,
        T)), I)), F, T, T)), subtract(center(extract(objects(I, T, T, T),
        compose(fork(equality, identity, rot90), rbind(subgrid, I)))),
        center(extract(objects(hmirror(subgrid(first(objects(I, F, T, T)),
        I)), T, T, T), compose(fork(equality, identity, rot90), rbind(
        subgrid, I))))))))), T, T, T), matcher(color, color(extract(objects
        (I, T, T, T), compose(fork(equality, identity, rot90), rbind(
        subgrid, I))))))))))


def solve_508bd3b6(I):
    return paint(paint(fill(paint(fill(I, THREE, connect(add(branch(
        equality(index(I, ulcorner(argmin(objects(I, T, T, T), size))),
        EIGHT), ulcorner(argmin(objects(I, T, T, T), size)), urcorner(
        argmin(objects(I, T, T, T), size))), double(multiply(branch(
        equality(index(I, ulcorner(argmin(objects(I, T, T, T), size))),
        EIGHT), UNITY, DOWN_LEFT), width(I)))), subtract(branch(equality(
        index(I, ulcorner(argmin(objects(I, T, T, T), size))), EIGHT),
        ulcorner(argmin(objects(I, T, T, T), size)), urcorner(argmin(
        objects(I, T, T, T), size))), double(multiply(branch(equality(index
        (I, ulcorner(argmin(objects(I, T, T, T), size))), EIGHT), UNITY,
        DOWN_LEFT), width(I)))))), argmax(objects(I, T, T, T), size)),
        THREE, connect(add(last(first(extract(objects(paint(fill(I, THREE,
        connect(add(branch(equality(index(I, ulcorner(argmin(objects(I, T,
        T, T), size))), EIGHT), ulcorner(argmin(objects(I, T, T, T), size)),
        urcorner(argmin(objects(I, T, T, T), size))), double(multiply(
        branch(equality(index(I, ulcorner(argmin(objects(I, T, T, T), size)
        )), EIGHT), UNITY, DOWN_LEFT), width(I)))), subtract(branch(
        equality(index(I, ulcorner(argmin(objects(I, T, T, T), size))),
        EIGHT), ulcorner(argmin(objects(I, T, T, T), size)), urcorner(
        argmin(objects(I, T, T, T), size))), double(multiply(branch(
        equality(index(I, ulcorner(argmin(objects(I, T, T, T), size))),
        EIGHT), UNITY, DOWN_LEFT), width(I)))))), argmax(objects(I, T, T, T
        ), size)), T, F, T), rbind(adjacent, argmax(objects(I, T, T, T),
        size))))), double(multiply(branch(flip(equality(index(I, ulcorner(
        argmin(objects(I, T, T, T), size))), EIGHT)), UNITY, DOWN_LEFT),
        width(I)))), subtract(last(first(extract(objects(paint(fill(I,
        THREE, connect(add(branch(equality(index(I, ulcorner(argmin(objects
        (I, T, T, T), size))), EIGHT), ulcorner(argmin(objects(I, T, T, T),
        size)), urcorner(argmin(objects(I, T, T, T), size))), double(
        multiply(branch(equality(index(I, ulcorner(argmin(objects(I, T, T,
        T), size))), EIGHT), UNITY, DOWN_LEFT), width(I)))), subtract(
        branch(equality(index(I, ulcorner(argmin(objects(I, T, T, T), size)
        )), EIGHT), ulcorner(argmin(objects(I, T, T, T), size)), urcorner(
        argmin(objects(I, T, T, T), size))), double(multiply(branch(
        equality(index(I, ulcorner(argmin(objects(I, T, T, T), size))),
        EIGHT), UNITY, DOWN_LEFT), width(I)))))), argmax(objects(I, T, T, T
        ), size)), T, F, T), rbind(adjacent, argmax(objects(I, T, T, T),
        size))))), double(multiply(branch(flip(equality(index(I, ulcorner(
        argmin(objects(I, T, T, T), size))), EIGHT)), UNITY, DOWN_LEFT),
        width(I)))))), argmin(objects(I, T, T, T), size)), argmax(objects(I,
        T, T, T), size))


def solve_6d0160f0(I):
    return paint(paint(I, mapply(lbind(shift, recolor(ZERO, asindices(crop(
        I, ORIGIN, THREE_BY_THREE)))), product(insert(EIGHT, insert(FOUR,
        initset(ZERO))), insert(EIGHT, insert(FOUR, initset(ZERO)))))),
        shift(toobject(asindices(replace(crop(I, astuple(branch(greater(
        first(first(ofcolor(I, FOUR))), SEVEN), EIGHT, branch(greater(first
        (first(ofcolor(I, FOUR))), THREE), FOUR, ZERO)), branch(greater(
        last(first(ofcolor(I, FOUR))), SEVEN), EIGHT, branch(greater(last(
        first(ofcolor(I, FOUR))), THREE), FOUR, ZERO))), THREE_BY_THREE),
        FIVE, ZERO)), replace(crop(I, astuple(branch(greater(first(first(
        ofcolor(I, FOUR))), SEVEN), EIGHT, branch(greater(first(first(
        ofcolor(I, FOUR))), THREE), FOUR, ZERO)), branch(greater(last(first
        (ofcolor(I, FOUR))), SEVEN), EIGHT, branch(greater(last(first(
        ofcolor(I, FOUR))), THREE), FOUR, ZERO))), THREE_BY_THREE), FIVE,
        ZERO)), multiply(first(ofcolor(replace(crop(I, astuple(branch(
        greater(first(first(ofcolor(I, FOUR))), SEVEN), EIGHT, branch(
        greater(first(first(ofcolor(I, FOUR))), THREE), FOUR, ZERO)),
        branch(greater(last(first(ofcolor(I, FOUR))), SEVEN), EIGHT, branch
        (greater(last(first(ofcolor(I, FOUR))), THREE), FOUR, ZERO))),
        THREE_BY_THREE), FIVE, ZERO), FOUR)), FOUR)))


def solve_f8a8fe49(I):
    return paint(paint(replace(I, FIVE, ZERO), shift(shift(last(apply(
        compose(normalize, asobject), apply_func(branch(portrait(first(
        colorfilter(objects(I, T, F, T), TWO))), hsplit, vsplit),
        apply_func(branch(portrait(first(colorfilter(objects(I, T, F, T),
        TWO))), vmirror, hmirror), trim(subgrid(ofcolor(I, TWO), I))), TWO)
        )), increment(ulcorner(ofcolor(I, TWO)))), invert(apply_func(
        compose(branch(portrait(first(colorfilter(objects(I, T, F, T), TWO)
        )), tojvec, toivec), increment), apply_func(branch(portrait(first(
        colorfilter(objects(I, T, F, T), TWO))), width, height), last(apply
        (compose(normalize, asobject), apply_func(branch(portrait(first(
        colorfilter(objects(I, T, F, T), TWO))), hsplit, vsplit),
        apply_func(branch(portrait(first(colorfilter(objects(I, T, F, T),
        TWO))), vmirror, hmirror), trim(subgrid(ofcolor(I, TWO), I))), TWO)
        ))))))), shift(shift(first(apply(compose(normalize, asobject),
        apply_func(branch(portrait(first(colorfilter(objects(I, T, F, T),
        TWO))), hsplit, vsplit), apply_func(branch(portrait(first(
        colorfilter(objects(I, T, F, T), TWO))), vmirror, hmirror), trim(
        subgrid(ofcolor(I, TWO), I))), TWO))), increment(ulcorner(ofcolor(I,
        TWO)))), apply_func(compose(branch(portrait(first(colorfilter(
        objects(I, T, F, T), TWO))), tojvec, toivec), increment), double(
        apply_func(branch(portrait(first(colorfilter(objects(I, T, F, T),
        TWO))), width, height), last(apply(compose(normalize, asobject),
        apply_func(branch(portrait(first(colorfilter(objects(I, T, F, T),
        TWO))), hsplit, vsplit), apply_func(branch(portrait(first(
        colorfilter(objects(I, T, F, T), TWO))), vmirror, hmirror), trim(
        subgrid(ofcolor(I, TWO), I))), TWO))))))))


def solve_d07ae81c(I):
    return fill(fill(I, branch(equality(mostcolor(toobject(neighbors(center
        (first(sizefilter(objects(I, T, F, F), ONE)))), I)), first(apply(
        color, difference(objects(I, T, F, F), sizefilter(objects(I, T, F,
        F), ONE))))), color(first(sizefilter(objects(I, T, F, F), ONE))),
        other(apply(color, sizefilter(objects(I, T, F, F), ONE)), color(
        first(sizefilter(objects(I, T, F, F), ONE))))), intersection(
        ofcolor(I, first(apply(color, difference(objects(I, T, F, F),
        sizefilter(objects(I, T, F, F), ONE))))), mapply(compose(fork(
        combine, fork(combine, rbind(shoot, UNITY), rbind(shoot, NEG_UNITY)
        ), fork(combine, rbind(shoot, DOWN_LEFT), rbind(shoot, UP_RIGHT))),
        center), sizefilter(objects(I, T, F, F), ONE)))), branch(equality(
        mostcolor(toobject(neighbors(center(first(sizefilter(objects(I, T,
        F, F), ONE)))), I)), first(apply(color, difference(objects(I, T, F,
        F), sizefilter(objects(I, T, F, F), ONE))))), other(apply(color,
        sizefilter(objects(I, T, F, F), ONE)), color(first(sizefilter(
        objects(I, T, F, F), ONE)))), color(first(sizefilter(objects(I, T,
        F, F), ONE)))), intersection(ofcolor(I, last(apply(color,
        difference(objects(I, T, F, F), sizefilter(objects(I, T, F, F), ONE
        ))))), mapply(compose(fork(combine, fork(combine, rbind(shoot,
        UNITY), rbind(shoot, NEG_UNITY)), fork(combine, rbind(shoot,
        DOWN_LEFT), rbind(shoot, UP_RIGHT))), center), sizefilter(objects(I,
        T, F, F), ONE))))


def solve_6a1e5592(I):
    return fill(cover(I, merge(colorfilter(objects(I, T, F, T), FIVE))),
        ONE, mapply(chain(rbind(argmax, fork(subtract, fork(subtract, fork(
        subtract, fork(add, chain(rbind(multiply, TEN), size, rbind(
        intersection, asindices(crop(I, ORIGIN, astuple(FIVE, width(I)))))),
        compose(invert, chain(rbind(multiply, TEN), size, rbind(
        intersection, ofcolor(crop(I, ORIGIN, astuple(FIVE, width(I))), TWO
        ))))), chain(size, rbind(intersection, ofcolor(crop(I, ORIGIN,
        astuple(FIVE, width(I))), ZERO)), outbox)), compose(rbind(multiply,
        EIGHT), uppermost)), chain(size, rbind(intersection, ofcolor(crop(I,
        ORIGIN, astuple(FIVE, width(I))), ZERO)), delta))), rbind(apply,
        asindices(crop(I, ORIGIN, astuple(FIVE, width(I))))), lbind(lbind,
        shift)), apply(compose(toindices, normalize), colorfilter(objects(I,
        T, F, T), FIVE))))


def solve_0e206a2e(I):
    return cover(paint(I, mapply(fork(mapply, compose(lbind(lbind, shift),
        normalize), fork(apply, chain(compose(lbind(rbind, subtract),
        ulcorner), rbind(sfilter, compose(rbind(contained, remove(argmax(
        remove(ZERO, palette(I)), lbind(colorcount, I)), remove(ZERO,
        palette(I)))), first)), normalize), chain(lbind(occurrences, I),
        rbind(sfilter, compose(rbind(contained, remove(argmax(remove(ZERO,
        palette(I)), lbind(colorcount, I)), remove(ZERO, palette(I)))),
        first)), normalize))), mapply(lbind(rapply, combine(combine(astuple
        (cmirror, dmirror), astuple(hmirror, vmirror)), totuple(apply(fork(
        compose, first, last), product(combine(astuple(cmirror, dmirror),
        astuple(hmirror, vmirror)), combine(astuple(cmirror, dmirror),
        astuple(hmirror, vmirror))))))), sfilter(objects(I, F, F, T),
        compose(rbind(greater, ONE), numcolors))))), merge(sfilter(objects(
        I, F, F, T), compose(rbind(greater, ONE), numcolors))))


def solve_d22278a0(I):
    return paint(I, mapply(fork(recolor, color, fork(intersection, fork(
        intersection, chain(lbind(sfilter, asindices(I)), lbind(compose,
        compose(chain(even, maximum, lbind(apply, fork(multiply, sign,
        identity))), fork(subtract, first, compose(center, last)))), lbind(
        rbind, astuple)), chain(lbind(sfilter, asindices(I)), rbind(compose,
        compose(lbind(argmin, objects(I, T, F, T)), compose(lbind(compose,
        chain(fork(add, first, last), lbind(apply, fork(multiply, sign,
        identity)), fork(subtract, first, compose(center, last)))), lbind(
        lbind, astuple)))), lbind(rbind, equality))), compose(lbind(sfilter,
        asindices(I)), fork(lbind(fork, greater), chain(rbind(compose,
        compose(lbind(compose, chain(fork(add, first, last), lbind(apply,
        fork(multiply, sign, identity)), fork(subtract, first, compose(
        center, last)))), lbind(lbind, astuple))), lbind(lbind, valmin),
        rbind(remove, objects(I, T, F, T))), compose(lbind(compose, chain(
        fork(add, first, last), lbind(apply, fork(multiply, sign, identity)
        ), fork(subtract, first, compose(center, last)))), lbind(rbind,
        astuple)))))), objects(I, T, F, T)))


def solve_4290ef0e(I):
    return paint(rot90(paint(rot90(paint(rot90(paint(canvas(mostcolor(I),
        astuple(decrement(double(branch(contained(ONE, apply(size,
        fgpartition(I))), size(fgpartition(I)), increment(size(fgpartition(
        I)))))), decrement(double(branch(contained(ONE, apply(size,
        fgpartition(I))), size(fgpartition(I)), increment(size(fgpartition(
        I)))))))), mpapply(shift, apply(normalize, apply(compose(rbind(
        argmin, centerofmass), fork(insert, hmirror, fork(insert, cmirror,
        fork(insert, dmirror, compose(initset, vmirror))))), order(
        fgpartition(I), compose(invert, fork(add, compose(maximum, shape),
        chain(rbind(valmax, width), lbind(colorfilter, objects(I, T, F, T)),
        color)))))), pair(interval(ZERO, branch(contained(ONE, apply(size,
        fgpartition(I))), size(fgpartition(I)), increment(size(fgpartition(
        I)))), ONE), interval(ZERO, branch(contained(ONE, apply(size,
        fgpartition(I))), size(fgpartition(I)), increment(size(fgpartition(
        I)))), ONE))))), mpapply(shift, apply(normalize, apply(compose(
        rbind(argmin, centerofmass), fork(insert, hmirror, fork(insert,
        cmirror, fork(insert, dmirror, compose(initset, vmirror))))), order
        (fgpartition(I), compose(invert, fork(add, compose(maximum, shape),
        chain(rbind(valmax, width), lbind(colorfilter, objects(I, T, F, T)),
        color)))))), pair(interval(ZERO, branch(contained(ONE, apply(size,
        fgpartition(I))), size(fgpartition(I)), increment(size(fgpartition(
        I)))), ONE), interval(ZERO, branch(contained(ONE, apply(size,
        fgpartition(I))), size(fgpartition(I)), increment(size(fgpartition(
        I)))), ONE))))), mpapply(shift, apply(normalize, apply(compose(
        rbind(argmin, centerofmass), fork(insert, hmirror, fork(insert,
        cmirror, fork(insert, dmirror, compose(initset, vmirror))))), order
        (fgpartition(I), compose(invert, fork(add, compose(maximum, shape),
        chain(rbind(valmax, width), lbind(colorfilter, objects(I, T, F, T)),
        color)))))), pair(interval(ZERO, branch(contained(ONE, apply(size,
        fgpartition(I))), size(fgpartition(I)), increment(size(fgpartition(
        I)))), ONE), interval(ZERO, branch(contained(ONE, apply(size,
        fgpartition(I))), size(fgpartition(I)), increment(size(fgpartition(
        I)))), ONE))))), mpapply(shift, apply(normalize, apply(compose(
        rbind(argmin, centerofmass), fork(insert, hmirror, fork(insert,
        cmirror, fork(insert, dmirror, compose(initset, vmirror))))), order
        (fgpartition(I), compose(invert, fork(add, compose(maximum, shape),
        chain(rbind(valmax, width), lbind(colorfilter, objects(I, T, F, T)),
        color)))))), pair(interval(ZERO, branch(contained(ONE, apply(size,
        fgpartition(I))), size(fgpartition(I)), increment(size(fgpartition(
        I)))), ONE), interval(ZERO, branch(contained(ONE, apply(size,
        fgpartition(I))), size(fgpartition(I)), increment(size(fgpartition(
        I)))), ONE))))


def solve_50846271(I):
    return fill(fill(fill(I, TWO, mfilter(prapply(connect, ofcolor(I, TWO),
        ofcolor(I, TWO)), fork(both, compose(lbind(greater, SIX), size),
        fork(either, vline, hline)))), EIGHT, mapply(fork(combine, fork(
        connect, rbind(add, toivec(halve(valmax(colorfilter(objects(fill(I,
        TWO, mfilter(prapply(connect, ofcolor(I, TWO), ofcolor(I, TWO)),
        fork(both, compose(lbind(greater, SIX), size), fork(either, vline,
        hline)))), T, F, F), TWO), width)))), rbind(subtract, toivec(halve(
        valmax(colorfilter(objects(fill(I, TWO, mfilter(prapply(connect,
        ofcolor(I, TWO), ofcolor(I, TWO)), fork(both, compose(lbind(greater,
        SIX), size), fork(either, vline, hline)))), T, F, F), TWO), width))
        ))), fork(connect, rbind(add, tojvec(halve(valmax(colorfilter(
        objects(fill(I, TWO, mfilter(prapply(connect, ofcolor(I, TWO),
        ofcolor(I, TWO)), fork(both, compose(lbind(greater, SIX), size),
        fork(either, vline, hline)))), T, F, F), TWO), width)))), rbind(
        subtract, tojvec(halve(valmax(colorfilter(objects(fill(I, TWO,
        mfilter(prapply(connect, ofcolor(I, TWO), ofcolor(I, TWO)), fork(
        both, compose(lbind(greater, SIX), size), fork(either, vline, hline
        )))), T, F, F), TWO), width)))))), apply(compose(rbind(argmax,
        chain(rbind(colorcount, TWO), rbind(toobject, fill(I, TWO, mfilter(
        prapply(connect, ofcolor(I, TWO), ofcolor(I, TWO)), fork(both,
        compose(lbind(greater, SIX), size), fork(either, vline, hline))))),
        fork(combine, dneighbors, fork(insert, rbind(subtract, TWO_BY_ZERO),
        fork(insert, rbind(subtract, ZERO_BY_TWO), fork(insert, rbind(add,
        TWO_BY_ZERO), compose(initset, rbind(add, ZERO_BY_TWO)))))))),
        toindices), colorfilter(objects(fill(I, TWO, mfilter(prapply(
        connect, ofcolor(I, TWO), ofcolor(I, TWO)), fork(both, compose(
        lbind(greater, SIX), size), fork(either, vline, hline)))), T, F, F),
        TWO)))), TWO, ofcolor(I, TWO))


def solve_b527c5c6(I):
    return underfill(fill(I, TWO, mapply(fork(shoot, compose(center, rbind(
        sfilter, matcher(first, TWO))), fork(astuple, fork(add, compose(
        invert, fork(equality, compose(uppermost, rbind(sfilter, matcher(
        first, TWO))), uppermost)), fork(equality, compose(lowermost, rbind
        (sfilter, matcher(first, TWO))), lowermost)), fork(add, compose(
        invert, fork(equality, compose(leftmost, rbind(sfilter, matcher(
        first, TWO))), leftmost)), fork(equality, compose(rightmost, rbind(
        sfilter, matcher(first, TWO))), rightmost)))), objects(I, F, F, T))
        ), THREE, combine(mapply(fork(mapply, compose(lbind(lbind, shift),
        fork(shoot, compose(center, rbind(sfilter, matcher(first, TWO))),
        fork(astuple, fork(add, compose(invert, fork(equality, compose(
        uppermost, rbind(sfilter, matcher(first, TWO))), uppermost)), fork(
        equality, compose(lowermost, rbind(sfilter, matcher(first, TWO))),
        lowermost)), fork(add, compose(invert, fork(equality, compose(
        leftmost, rbind(sfilter, matcher(first, TWO))), leftmost)), fork(
        equality, compose(rightmost, rbind(sfilter, matcher(first, TWO))),
        rightmost))))), compose(lbind(apply, toivec), fork(rbind(interval,
        ONE), compose(invert, chain(decrement, minimum, shape)), compose(
        increment, chain(decrement, minimum, shape))))), difference(objects
        (I, F, F, T), sfilter(objects(I, F, F, T), compose(vline, fork(
        shoot, compose(center, rbind(sfilter, matcher(first, TWO))), fork(
        astuple, fork(add, compose(invert, fork(equality, compose(uppermost,
        rbind(sfilter, matcher(first, TWO))), uppermost)), fork(equality,
        compose(lowermost, rbind(sfilter, matcher(first, TWO))), lowermost)
        ), fork(add, compose(invert, fork(equality, compose(leftmost, rbind
        (sfilter, matcher(first, TWO))), leftmost)), fork(equality, compose
        (rightmost, rbind(sfilter, matcher(first, TWO))), rightmost)))))))),
        mapply(fork(mapply, compose(lbind(lbind, shift), fork(shoot,
        compose(center, rbind(sfilter, matcher(first, TWO))), fork(astuple,
        fork(add, compose(invert, fork(equality, compose(uppermost, rbind(
        sfilter, matcher(first, TWO))), uppermost)), fork(equality, compose
        (lowermost, rbind(sfilter, matcher(first, TWO))), lowermost)), fork
        (add, compose(invert, fork(equality, compose(leftmost, rbind(
        sfilter, matcher(first, TWO))), leftmost)), fork(equality, compose(
        rightmost, rbind(sfilter, matcher(first, TWO))), rightmost))))),
        compose(lbind(apply, tojvec), fork(rbind(interval, ONE), compose(
        invert, chain(decrement, minimum, shape)), compose(increment, chain
        (decrement, minimum, shape))))), sfilter(objects(I, F, F, T),
        compose(vline, fork(shoot, compose(center, rbind(sfilter, matcher(
        first, TWO))), fork(astuple, fork(add, compose(invert, fork(
        equality, compose(uppermost, rbind(sfilter, matcher(first, TWO))),
        uppermost)), fork(equality, compose(lowermost, rbind(sfilter,
        matcher(first, TWO))), lowermost)), fork(add, compose(invert, fork(
        equality, compose(leftmost, rbind(sfilter, matcher(first, TWO))),
        leftmost)), fork(equality, compose(rightmost, rbind(sfilter,
        matcher(first, TWO))), rightmost)))))))))


def solve_150deff5(I):
    return fill(fill(fill(fill(fill(fill(I, EIGHT, mapply(lbind(shift,
        asobject(canvas(FIVE, TWO_BY_TWO))), occurrences(I, asobject(canvas
        (FIVE, TWO_BY_TWO))))), TWO, mapply(lbind(shift, asobject(vconcat(
        canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))),
        occurrences(fill(I, EIGHT, mapply(lbind(shift, asobject(canvas(FIVE,
        TWO_BY_TWO))), occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))),
        asobject(vconcat(canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE,
        UNITY)))))), TWO, mapply(lbind(shift, asobject(canvas(FIVE, astuple
        (ONE, THREE)))), occurrences(fill(fill(I, EIGHT, mapply(lbind(shift,
        asobject(canvas(FIVE, TWO_BY_TWO))), occurrences(I, asobject(canvas
        (FIVE, TWO_BY_TWO))))), TWO, mapply(lbind(shift, asobject(vconcat(
        canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))),
        occurrences(fill(I, EIGHT, mapply(lbind(shift, asobject(canvas(FIVE,
        TWO_BY_TWO))), occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))),
        asobject(vconcat(canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE,
        UNITY)))))), asobject(canvas(FIVE, astuple(ONE, THREE)))))), TWO,
        mapply(lbind(shift, asobject(hmirror(vconcat(canvas(EIGHT, astuple(
        TWO, ONE)), canvas(FIVE, UNITY))))), occurrences(fill(fill(fill(I,
        EIGHT, mapply(lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))),
        occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))), TWO, mapply(
        lbind(shift, asobject(vconcat(canvas(EIGHT, astuple(TWO, ONE)),
        canvas(FIVE, UNITY)))), occurrences(fill(I, EIGHT, mapply(lbind(
        shift, asobject(canvas(FIVE, TWO_BY_TWO))), occurrences(I, asobject
        (canvas(FIVE, TWO_BY_TWO))))), asobject(vconcat(canvas(EIGHT,
        astuple(TWO, ONE)), canvas(FIVE, UNITY)))))), TWO, mapply(lbind(
        shift, asobject(canvas(FIVE, astuple(ONE, THREE)))), occurrences(
        fill(fill(I, EIGHT, mapply(lbind(shift, asobject(canvas(FIVE,
        TWO_BY_TWO))), occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))),
        TWO, mapply(lbind(shift, asobject(vconcat(canvas(EIGHT, astuple(TWO,
        ONE)), canvas(FIVE, UNITY)))), occurrences(fill(I, EIGHT, mapply(
        lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))), occurrences(I,
        asobject(canvas(FIVE, TWO_BY_TWO))))), asobject(vconcat(canvas(
        EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))))), asobject(
        canvas(FIVE, astuple(ONE, THREE)))))), asobject(hmirror(vconcat(
        canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY))))))), TWO,
        mapply(lbind(shift, asobject(dmirror(vconcat(canvas(EIGHT, astuple(
        TWO, ONE)), canvas(FIVE, UNITY))))), occurrences(fill(fill(fill(
        fill(I, EIGHT, mapply(lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO
        ))), occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))), TWO,
        mapply(lbind(shift, asobject(vconcat(canvas(EIGHT, astuple(TWO, ONE
        )), canvas(FIVE, UNITY)))), occurrences(fill(I, EIGHT, mapply(lbind
        (shift, asobject(canvas(FIVE, TWO_BY_TWO))), occurrences(I,
        asobject(canvas(FIVE, TWO_BY_TWO))))), asobject(vconcat(canvas(
        EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))))), TWO, mapply(
        lbind(shift, asobject(canvas(FIVE, astuple(ONE, THREE)))),
        occurrences(fill(fill(I, EIGHT, mapply(lbind(shift, asobject(canvas
        (FIVE, TWO_BY_TWO))), occurrences(I, asobject(canvas(FIVE,
        TWO_BY_TWO))))), TWO, mapply(lbind(shift, asobject(vconcat(canvas(
        EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))), occurrences(fill
        (I, EIGHT, mapply(lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))),
        occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))), asobject(
        vconcat(canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))))),
        asobject(canvas(FIVE, astuple(ONE, THREE)))))), TWO, mapply(lbind(
        shift, asobject(hmirror(vconcat(canvas(EIGHT, astuple(TWO, ONE)),
        canvas(FIVE, UNITY))))), occurrences(fill(fill(fill(I, EIGHT,
        mapply(lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))),
        occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))), TWO, mapply(
        lbind(shift, asobject(vconcat(canvas(EIGHT, astuple(TWO, ONE)),
        canvas(FIVE, UNITY)))), occurrences(fill(I, EIGHT, mapply(lbind(
        shift, asobject(canvas(FIVE, TWO_BY_TWO))), occurrences(I, asobject
        (canvas(FIVE, TWO_BY_TWO))))), asobject(vconcat(canvas(EIGHT,
        astuple(TWO, ONE)), canvas(FIVE, UNITY)))))), TWO, mapply(lbind(
        shift, asobject(canvas(FIVE, astuple(ONE, THREE)))), occurrences(
        fill(fill(I, EIGHT, mapply(lbind(shift, asobject(canvas(FIVE,
        TWO_BY_TWO))), occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))),
        TWO, mapply(lbind(shift, asobject(vconcat(canvas(EIGHT, astuple(TWO,
        ONE)), canvas(FIVE, UNITY)))), occurrences(fill(I, EIGHT, mapply(
        lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))), occurrences(I,
        asobject(canvas(FIVE, TWO_BY_TWO))))), asobject(vconcat(canvas(
        EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))))), asobject(
        canvas(FIVE, astuple(ONE, THREE)))))), asobject(hmirror(vconcat(
        canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY))))))),
        asobject(dmirror(vconcat(canvas(EIGHT, astuple(TWO, ONE)), canvas(
        FIVE, UNITY))))))), TWO, mapply(lbind(shift, asobject(vmirror(
        dmirror(vconcat(canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE,
        UNITY)))))), occurrences(fill(fill(fill(fill(fill(I, EIGHT, mapply(
        lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))), occurrences(I,
        asobject(canvas(FIVE, TWO_BY_TWO))))), TWO, mapply(lbind(shift,
        asobject(vconcat(canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE,
        UNITY)))), occurrences(fill(I, EIGHT, mapply(lbind(shift, asobject(
        canvas(FIVE, TWO_BY_TWO))), occurrences(I, asobject(canvas(FIVE,
        TWO_BY_TWO))))), asobject(vconcat(canvas(EIGHT, astuple(TWO, ONE)),
        canvas(FIVE, UNITY)))))), TWO, mapply(lbind(shift, asobject(canvas(
        FIVE, astuple(ONE, THREE)))), occurrences(fill(fill(I, EIGHT,
        mapply(lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))),
        occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))), TWO, mapply(
        lbind(shift, asobject(vconcat(canvas(EIGHT, astuple(TWO, ONE)),
        canvas(FIVE, UNITY)))), occurrences(fill(I, EIGHT, mapply(lbind(
        shift, asobject(canvas(FIVE, TWO_BY_TWO))), occurrences(I, asobject
        (canvas(FIVE, TWO_BY_TWO))))), asobject(vconcat(canvas(EIGHT,
        astuple(TWO, ONE)), canvas(FIVE, UNITY)))))), asobject(canvas(FIVE,
        astuple(ONE, THREE)))))), TWO, mapply(lbind(shift, asobject(hmirror
        (vconcat(canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY))))),
        occurrences(fill(fill(fill(I, EIGHT, mapply(lbind(shift, asobject(
        canvas(FIVE, TWO_BY_TWO))), occurrences(I, asobject(canvas(FIVE,
        TWO_BY_TWO))))), TWO, mapply(lbind(shift, asobject(vconcat(canvas(
        EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))), occurrences(fill
        (I, EIGHT, mapply(lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))),
        occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))), asobject(
        vconcat(canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))))),
        TWO, mapply(lbind(shift, asobject(canvas(FIVE, astuple(ONE, THREE))
        )), occurrences(fill(fill(I, EIGHT, mapply(lbind(shift, asobject(
        canvas(FIVE, TWO_BY_TWO))), occurrences(I, asobject(canvas(FIVE,
        TWO_BY_TWO))))), TWO, mapply(lbind(shift, asobject(vconcat(canvas(
        EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))), occurrences(fill
        (I, EIGHT, mapply(lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))),
        occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))), asobject(
        vconcat(canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))))),
        asobject(canvas(FIVE, astuple(ONE, THREE)))))), asobject(hmirror(
        vconcat(canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY))))))),
        TWO, mapply(lbind(shift, asobject(dmirror(vconcat(canvas(EIGHT,
        astuple(TWO, ONE)), canvas(FIVE, UNITY))))), occurrences(fill(fill(
        fill(fill(I, EIGHT, mapply(lbind(shift, asobject(canvas(FIVE,
        TWO_BY_TWO))), occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))),
        TWO, mapply(lbind(shift, asobject(vconcat(canvas(EIGHT, astuple(TWO,
        ONE)), canvas(FIVE, UNITY)))), occurrences(fill(I, EIGHT, mapply(
        lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))), occurrences(I,
        asobject(canvas(FIVE, TWO_BY_TWO))))), asobject(vconcat(canvas(
        EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))))), TWO, mapply(
        lbind(shift, asobject(canvas(FIVE, astuple(ONE, THREE)))),
        occurrences(fill(fill(I, EIGHT, mapply(lbind(shift, asobject(canvas
        (FIVE, TWO_BY_TWO))), occurrences(I, asobject(canvas(FIVE,
        TWO_BY_TWO))))), TWO, mapply(lbind(shift, asobject(vconcat(canvas(
        EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))), occurrences(fill
        (I, EIGHT, mapply(lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))),
        occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))), asobject(
        vconcat(canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))))),
        asobject(canvas(FIVE, astuple(ONE, THREE)))))), TWO, mapply(lbind(
        shift, asobject(hmirror(vconcat(canvas(EIGHT, astuple(TWO, ONE)),
        canvas(FIVE, UNITY))))), occurrences(fill(fill(fill(I, EIGHT,
        mapply(lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))),
        occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))), TWO, mapply(
        lbind(shift, asobject(vconcat(canvas(EIGHT, astuple(TWO, ONE)),
        canvas(FIVE, UNITY)))), occurrences(fill(I, EIGHT, mapply(lbind(
        shift, asobject(canvas(FIVE, TWO_BY_TWO))), occurrences(I, asobject
        (canvas(FIVE, TWO_BY_TWO))))), asobject(vconcat(canvas(EIGHT,
        astuple(TWO, ONE)), canvas(FIVE, UNITY)))))), TWO, mapply(lbind(
        shift, asobject(canvas(FIVE, astuple(ONE, THREE)))), occurrences(
        fill(fill(I, EIGHT, mapply(lbind(shift, asobject(canvas(FIVE,
        TWO_BY_TWO))), occurrences(I, asobject(canvas(FIVE, TWO_BY_TWO))))),
        TWO, mapply(lbind(shift, asobject(vconcat(canvas(EIGHT, astuple(TWO,
        ONE)), canvas(FIVE, UNITY)))), occurrences(fill(I, EIGHT, mapply(
        lbind(shift, asobject(canvas(FIVE, TWO_BY_TWO))), occurrences(I,
        asobject(canvas(FIVE, TWO_BY_TWO))))), asobject(vconcat(canvas(
        EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY)))))), asobject(
        canvas(FIVE, astuple(ONE, THREE)))))), asobject(hmirror(vconcat(
        canvas(EIGHT, astuple(TWO, ONE)), canvas(FIVE, UNITY))))))),
        asobject(dmirror(vconcat(canvas(EIGHT, astuple(TWO, ONE)), canvas(
        FIVE, UNITY))))))), asobject(vmirror(dmirror(vconcat(canvas(EIGHT,
        astuple(TWO, ONE)), canvas(FIVE, UNITY))))))))


def solve_b7249182(I):
    return apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), cover(fill(fill(paint(fill(fill(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), color
        (last(order(objects(apply_func(branch(portrait(merge(objects(I, T,
        F, T))), identity, dmirror), I), T, F, T), uppermost))), connect(
        apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))), color(first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), connect(apply_func(compose(first, toindices), first(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))), centerofmass(
        connect(apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))))), combine(shift(toobject(insert(add(centerofmass(connect(
        apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))), DOWN), initset(centerofmass(connect(apply_func(compose(first,
        toindices), first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), apply_func(compose(first, toindices), last(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))))))), fill(fill(apply_func(
        branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I),
        color(last(order(objects(apply_func(branch(portrait(merge(objects(I,
        T, F, T))), identity, dmirror), I), T, F, T), uppermost))), connect
        (apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))), color(first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), connect(apply_func(compose(first, toindices), first(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))), centerofmass(
        connect(apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        ))))))), ZERO_BY_TWO), shift(toobject(insert(add(centerofmass(
        connect(apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))), DOWN), initset(centerofmass(connect(apply_func(compose(first,
        toindices), first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), apply_func(compose(first, toindices), last(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))))))), fill(fill(apply_func(
        branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I),
        color(last(order(objects(apply_func(branch(portrait(merge(objects(I,
        T, F, T))), identity, dmirror), I), T, F, T), uppermost))), connect
        (apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))), color(first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), connect(apply_func(compose(first, toindices), first(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))), centerofmass(
        connect(apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        ))))))), astuple(ZERO, NEG_TWO)))), color(first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), shift(connect(ulcorner(
        combine(shift(toobject(insert(add(centerofmass(connect(apply_func(
        compose(first, toindices), first(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))), apply_func(compose(first, toindices), last(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))))), DOWN), initset(
        centerofmass(connect(apply_func(compose(first, toindices), first(
        order(objects(apply_func(branch(portrait(merge(objects(I, T, F, T))
        ), identity, dmirror), I), T, F, T), uppermost))), apply_func(
        compose(first, toindices), last(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))))))), fill(fill(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), color(last(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))), connect(apply_func(
        compose(first, toindices), first(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))), apply_func(compose(first, toindices), last(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))))), color(first(order
        (objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))), connect(apply_func(
        compose(first, toindices), first(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))), centerofmass(connect(apply_func(compose(first,
        toindices), first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), apply_func(compose(first, toindices), last(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost)))))))), ZERO_BY_TWO), shift(
        toobject(insert(add(centerofmass(connect(apply_func(compose(first,
        toindices), first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), apply_func(compose(first, toindices), last(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))))), DOWN), initset(centerofmass
        (connect(apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))))), fill(fill(apply_func(branch(portrait(merge(objects(I, T, F,
        T))), identity, dmirror), I), color(last(order(objects(apply_func(
        branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I),
        T, F, T), uppermost))), connect(apply_func(compose(first, toindices
        ), first(order(objects(apply_func(branch(portrait(merge(objects(I,
        T, F, T))), identity, dmirror), I), T, F, T), uppermost))),
        apply_func(compose(first, toindices), last(order(objects(apply_func
        (branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I
        ), T, F, T), uppermost))))), color(first(order(objects(apply_func(
        branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I),
        T, F, T), uppermost))), connect(apply_func(compose(first, toindices
        ), first(order(objects(apply_func(branch(portrait(merge(objects(I,
        T, F, T))), identity, dmirror), I), T, F, T), uppermost))),
        centerofmass(connect(apply_func(compose(first, toindices), first(
        order(objects(apply_func(branch(portrait(merge(objects(I, T, F, T))
        ), identity, dmirror), I), T, F, T), uppermost))), apply_func(
        compose(first, toindices), last(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost)))))))), astuple(ZERO, NEG_TWO)))), urcorner(combine(
        shift(toobject(insert(add(centerofmass(connect(apply_func(compose(
        first, toindices), first(order(objects(apply_func(branch(portrait(
        merge(objects(I, T, F, T))), identity, dmirror), I), T, F, T),
        uppermost))), apply_func(compose(first, toindices), last(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))))), DOWN), initset(
        centerofmass(connect(apply_func(compose(first, toindices), first(
        order(objects(apply_func(branch(portrait(merge(objects(I, T, F, T))
        ), identity, dmirror), I), T, F, T), uppermost))), apply_func(
        compose(first, toindices), last(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))))))), fill(fill(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), color(last(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))), connect(apply_func(
        compose(first, toindices), first(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))), apply_func(compose(first, toindices), last(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))))), color(first(order
        (objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))), connect(apply_func(
        compose(first, toindices), first(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))), centerofmass(connect(apply_func(compose(first,
        toindices), first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), apply_func(compose(first, toindices), last(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost)))))))), ZERO_BY_TWO), shift(
        toobject(insert(add(centerofmass(connect(apply_func(compose(first,
        toindices), first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), apply_func(compose(first, toindices), last(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))))), DOWN), initset(centerofmass
        (connect(apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))))), fill(fill(apply_func(branch(portrait(merge(objects(I, T, F,
        T))), identity, dmirror), I), color(last(order(objects(apply_func(
        branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I),
        T, F, T), uppermost))), connect(apply_func(compose(first, toindices
        ), first(order(objects(apply_func(branch(portrait(merge(objects(I,
        T, F, T))), identity, dmirror), I), T, F, T), uppermost))),
        apply_func(compose(first, toindices), last(order(objects(apply_func
        (branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I
        ), T, F, T), uppermost))))), color(first(order(objects(apply_func(
        branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I),
        T, F, T), uppermost))), connect(apply_func(compose(first, toindices
        ), first(order(objects(apply_func(branch(portrait(merge(objects(I,
        T, F, T))), identity, dmirror), I), T, F, T), uppermost))),
        centerofmass(connect(apply_func(compose(first, toindices), first(
        order(objects(apply_func(branch(portrait(merge(objects(I, T, F, T))
        ), identity, dmirror), I), T, F, T), uppermost))), apply_func(
        compose(first, toindices), last(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost)))))))), astuple(ZERO, NEG_TWO))))), UP)), color(last
        (order(objects(apply_func(branch(portrait(merge(objects(I, T, F, T)
        )), identity, dmirror), I), T, F, T), uppermost))), shift(connect(
        llcorner(combine(shift(toobject(insert(add(centerofmass(connect(
        apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))), DOWN), initset(centerofmass(connect(apply_func(compose(first,
        toindices), first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), apply_func(compose(first, toindices), last(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))))))), fill(fill(apply_func(
        branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I),
        color(last(order(objects(apply_func(branch(portrait(merge(objects(I,
        T, F, T))), identity, dmirror), I), T, F, T), uppermost))), connect
        (apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))), color(first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), connect(apply_func(compose(first, toindices), first(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))), centerofmass(
        connect(apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        ))))))), ZERO_BY_TWO), shift(toobject(insert(add(centerofmass(
        connect(apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))), DOWN), initset(centerofmass(connect(apply_func(compose(first,
        toindices), first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), apply_func(compose(first, toindices), last(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))))))), fill(fill(apply_func(
        branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I),
        color(last(order(objects(apply_func(branch(portrait(merge(objects(I,
        T, F, T))), identity, dmirror), I), T, F, T), uppermost))), connect
        (apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))), color(first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), connect(apply_func(compose(first, toindices), first(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))), centerofmass(
        connect(apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        ))))))), astuple(ZERO, NEG_TWO)))), lrcorner(combine(shift(toobject
        (insert(add(centerofmass(connect(apply_func(compose(first,
        toindices), first(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )), apply_func(compose(first, toindices), last(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))))), DOWN), initset(centerofmass
        (connect(apply_func(compose(first, toindices), first(order(objects(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), T, F, T), uppermost))), apply_func(compose(first,
        toindices), last(order(objects(apply_func(branch(portrait(merge(
        objects(I, T, F, T))), identity, dmirror), I), T, F, T), uppermost)
        )))))), fill(fill(apply_func(branch(portrait(merge(objects(I, T, F,
        T))), identity, dmirror), I), color(last(order(objects(apply_func(
        branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I),
        T, F, T), uppermost))), connect(apply_func(compose(first, toindices
        ), first(order(objects(apply_func(branch(portrait(merge(objects(I,
        T, F, T))), identity, dmirror), I), T, F, T), uppermost))),
        apply_func(compose(first, toindices), last(order(objects(apply_func
        (branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I
        ), T, F, T), uppermost))))), color(first(order(objects(apply_func(
        branch(portrait(merge(objects(I, T, F, T))), identity, dmirror), I),
        T, F, T), uppermost))), connect(apply_func(compose(first, toindices
        ), first(order(objects(apply_func(branch(portrait(merge(objects(I,
        T, F, T))), identity, dmirror), I), T, F, T), uppermost))),
        centerofmass(connect(apply_func(compose(first, toindices), first(
        order(objects(apply_func(branch(portrait(merge(objects(I, T, F, T))
        ), identity, dmirror), I), T, F, T), uppermost))), apply_func(
        compose(first, toindices), last(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost)))))))), ZERO_BY_TWO), shift(toobject(insert(add(
        centerofmass(connect(apply_func(compose(first, toindices), first(
        order(objects(apply_func(branch(portrait(merge(objects(I, T, F, T))
        ), identity, dmirror), I), T, F, T), uppermost))), apply_func(
        compose(first, toindices), last(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))))), DOWN), initset(centerofmass(connect(apply_func(
        compose(first, toindices), first(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))), apply_func(compose(first, toindices), last(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost))))))), fill(fill(
        apply_func(branch(portrait(merge(objects(I, T, F, T))), identity,
        dmirror), I), color(last(order(objects(apply_func(branch(portrait(
        merge(objects(I, T, F, T))), identity, dmirror), I), T, F, T),
        uppermost))), connect(apply_func(compose(first, toindices), first(
        order(objects(apply_func(branch(portrait(merge(objects(I, T, F, T))
        ), identity, dmirror), I), T, F, T), uppermost))), apply_func(
        compose(first, toindices), last(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))))), color(first(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))), connect(apply_func(compose(first, toindices),
        first(order(objects(apply_func(branch(portrait(merge(objects(I, T,
        F, T))), identity, dmirror), I), T, F, T), uppermost))),
        centerofmass(connect(apply_func(compose(first, toindices), first(
        order(objects(apply_func(branch(portrait(merge(objects(I, T, F, T))
        ), identity, dmirror), I), T, F, T), uppermost))), apply_func(
        compose(first, toindices), last(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost)))))))), astuple(ZERO, NEG_TWO))))), DOWN)), insert(
        add(centerofmass(connect(apply_func(compose(first, toindices),
        first(order(objects(apply_func(branch(portrait(merge(objects(I, T,
        F, T))), identity, dmirror), I), T, F, T), uppermost))), apply_func
        (compose(first, toindices), last(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))))), DOWN), initset(centerofmass(connect(apply_func(
        compose(first, toindices), first(order(objects(apply_func(branch(
        portrait(merge(objects(I, T, F, T))), identity, dmirror), I), T, F,
        T), uppermost))), apply_func(compose(first, toindices), last(order(
        objects(apply_func(branch(portrait(merge(objects(I, T, F, T))),
        identity, dmirror), I), T, F, T), uppermost)))))))))


def solve_9d9215db(I):
    return apply(lbind(apply, maximum), papply(pair, apply(lbind(apply,
        maximum), papply(pair, apply(lbind(apply, maximum), papply(pair,
        paint(cover(apply(lbind(apply, maximum), papply(pair, argmax(insert
        (rot270(I), insert(rot180(I), insert(rot90(I), initset(I)))), chain
        (numcolors, lefthalf, tophalf)), vmirror(argmax(insert(rot270(I),
        insert(rot180(I), insert(rot90(I), initset(I)))), chain(numcolors,
        lefthalf, tophalf))))), combine(apply(llcorner, sizefilter(
        partition(apply(lbind(apply, maximum), papply(pair, argmax(insert(
        rot270(I), insert(rot180(I), insert(rot90(I), initset(I)))), chain(
        numcolors, lefthalf, tophalf)), vmirror(argmax(insert(rot270(I),
        insert(rot180(I), insert(rot90(I), initset(I)))), chain(numcolors,
        lefthalf, tophalf)))))), FOUR)), apply(lrcorner, sizefilter(
        partition(apply(lbind(apply, maximum), papply(pair, argmax(insert(
        rot270(I), insert(rot180(I), insert(rot90(I), initset(I)))), chain(
        numcolors, lefthalf, tophalf)), vmirror(argmax(insert(rot270(I),
        insert(rot180(I), insert(rot90(I), initset(I)))), chain(numcolors,
        lefthalf, tophalf)))))), FOUR)))), mapply(fork(recolor, color, fork
        (shift, chain(normalize, rbind(sfilter, compose(even, last)), fork(
        connect, compose(rbind(add, ZERO_BY_TWO), ulcorner), compose(rbind(
        add, tojvec(NEG_TWO)), urcorner))), compose(rbind(add, ZERO_BY_TWO),
        ulcorner))), sizefilter(partition(apply(lbind(apply, maximum),
        papply(pair, argmax(insert(rot270(I), insert(rot180(I), insert(
        rot90(I), initset(I)))), chain(numcolors, lefthalf, tophalf)),
        vmirror(argmax(insert(rot270(I), insert(rot180(I), insert(rot90(I),
        initset(I)))), chain(numcolors, lefthalf, tophalf)))))), FOUR))),
        rot90(paint(cover(apply(lbind(apply, maximum), papply(pair, argmax(
        insert(rot270(I), insert(rot180(I), insert(rot90(I), initset(I)))),
        chain(numcolors, lefthalf, tophalf)), vmirror(argmax(insert(rot270(
        I), insert(rot180(I), insert(rot90(I), initset(I)))), chain(
        numcolors, lefthalf, tophalf))))), combine(apply(llcorner,
        sizefilter(partition(apply(lbind(apply, maximum), papply(pair,
        argmax(insert(rot270(I), insert(rot180(I), insert(rot90(I), initset
        (I)))), chain(numcolors, lefthalf, tophalf)), vmirror(argmax(insert
        (rot270(I), insert(rot180(I), insert(rot90(I), initset(I)))), chain
        (numcolors, lefthalf, tophalf)))))), FOUR)), apply(lrcorner,
        sizefilter(partition(apply(lbind(apply, maximum), papply(pair,
        argmax(insert(rot270(I), insert(rot180(I), insert(rot90(I), initset
        (I)))), chain(numcolors, lefthalf, tophalf)), vmirror(argmax(insert
        (rot270(I), insert(rot180(I), insert(rot90(I), initset(I)))), chain
        (numcolors, lefthalf, tophalf)))))), FOUR)))), mapply(fork(recolor,
        color, fork(shift, chain(normalize, rbind(sfilter, compose(even,
        last)), fork(connect, compose(rbind(add, ZERO_BY_TWO), ulcorner),
        compose(rbind(add, tojvec(NEG_TWO)), urcorner))), compose(rbind(add,
        ZERO_BY_TWO), ulcorner))), sizefilter(partition(apply(lbind(apply,
        maximum), papply(pair, argmax(insert(rot270(I), insert(rot180(I),
        insert(rot90(I), initset(I)))), chain(numcolors, lefthalf, tophalf)
        ), vmirror(argmax(insert(rot270(I), insert(rot180(I), insert(rot90(
        I), initset(I)))), chain(numcolors, lefthalf, tophalf)))))), FOUR))
        )))), rot180(paint(cover(apply(lbind(apply, maximum), papply(pair,
        argmax(insert(rot270(I), insert(rot180(I), insert(rot90(I), initset
        (I)))), chain(numcolors, lefthalf, tophalf)), vmirror(argmax(insert
        (rot270(I), insert(rot180(I), insert(rot90(I), initset(I)))), chain
        (numcolors, lefthalf, tophalf))))), combine(apply(llcorner,
        sizefilter(partition(apply(lbind(apply, maximum), papply(pair,
        argmax(insert(rot270(I), insert(rot180(I), insert(rot90(I), initset
        (I)))), chain(numcolors, lefthalf, tophalf)), vmirror(argmax(insert
        (rot270(I), insert(rot180(I), insert(rot90(I), initset(I)))), chain
        (numcolors, lefthalf, tophalf)))))), FOUR)), apply(lrcorner,
        sizefilter(partition(apply(lbind(apply, maximum), papply(pair,
        argmax(insert(rot270(I), insert(rot180(I), insert(rot90(I), initset
        (I)))), chain(numcolors, lefthalf, tophalf)), vmirror(argmax(insert
        (rot270(I), insert(rot180(I), insert(rot90(I), initset(I)))), chain
        (numcolors, lefthalf, tophalf)))))), FOUR)))), mapply(fork(recolor,
        color, fork(shift, chain(normalize, rbind(sfilter, compose(even,
        last)), fork(connect, compose(rbind(add, ZERO_BY_TWO), ulcorner),
        compose(rbind(add, tojvec(NEG_TWO)), urcorner))), compose(rbind(add,
        ZERO_BY_TWO), ulcorner))), sizefilter(partition(apply(lbind(apply,
        maximum), papply(pair, argmax(insert(rot270(I), insert(rot180(I),
        insert(rot90(I), initset(I)))), chain(numcolors, lefthalf, tophalf)
        ), vmirror(argmax(insert(rot270(I), insert(rot180(I), insert(rot90(
        I), initset(I)))), chain(numcolors, lefthalf, tophalf)))))), FOUR))
        )))), rot270(paint(cover(apply(lbind(apply, maximum), papply(pair,
        argmax(insert(rot270(I), insert(rot180(I), insert(rot90(I), initset
        (I)))), chain(numcolors, lefthalf, tophalf)), vmirror(argmax(insert
        (rot270(I), insert(rot180(I), insert(rot90(I), initset(I)))), chain
        (numcolors, lefthalf, tophalf))))), combine(apply(llcorner,
        sizefilter(partition(apply(lbind(apply, maximum), papply(pair,
        argmax(insert(rot270(I), insert(rot180(I), insert(rot90(I), initset
        (I)))), chain(numcolors, lefthalf, tophalf)), vmirror(argmax(insert
        (rot270(I), insert(rot180(I), insert(rot90(I), initset(I)))), chain
        (numcolors, lefthalf, tophalf)))))), FOUR)), apply(lrcorner,
        sizefilter(partition(apply(lbind(apply, maximum), papply(pair,
        argmax(insert(rot270(I), insert(rot180(I), insert(rot90(I), initset
        (I)))), chain(numcolors, lefthalf, tophalf)), vmirror(argmax(insert
        (rot270(I), insert(rot180(I), insert(rot90(I), initset(I)))), chain
        (numcolors, lefthalf, tophalf)))))), FOUR)))), mapply(fork(recolor,
        color, fork(shift, chain(normalize, rbind(sfilter, compose(even,
        last)), fork(connect, compose(rbind(add, ZERO_BY_TWO), ulcorner),
        compose(rbind(add, tojvec(NEG_TWO)), urcorner))), compose(rbind(add,
        ZERO_BY_TWO), ulcorner))), sizefilter(partition(apply(lbind(apply,
        maximum), papply(pair, argmax(insert(rot270(I), insert(rot180(I),
        insert(rot90(I), initset(I)))), chain(numcolors, lefthalf, tophalf)
        ), vmirror(argmax(insert(rot270(I), insert(rot180(I), insert(rot90(
        I), initset(I)))), chain(numcolors, lefthalf, tophalf)))))), FOUR))))))


def solve_6855a6e4(I):
    return branch(portrait(first(colorfilter(fgpartition(I), TWO))), paint(
        paint(cover(branch(portrait(first(colorfilter(fgpartition(I), TWO))
        ), I, rot90(I)), merge(colorfilter(objects(branch(portrait(first(
        colorfilter(fgpartition(I), TWO))), I, rot90(I)), T, F, T), FIVE))),
        shift(recolor(FIVE, ofcolor(hmirror(subgrid(extract(colorfilter(
        objects(branch(portrait(first(colorfilter(fgpartition(I), TWO))), I,
        rot90(I)), T, F, T), FIVE), matcher(compose(first, center), valmin(
        apply(center, colorfilter(objects(branch(portrait(first(colorfilter
        (fgpartition(I), TWO))), I, rot90(I)), T, F, T), FIVE)), first))),
        branch(portrait(first(colorfilter(fgpartition(I), TWO))), I, rot90(
        I)))), FIVE)), add(ulcorner(extract(colorfilter(objects(branch(
        portrait(first(colorfilter(fgpartition(I), TWO))), I, rot90(I)), T,
        F, T), FIVE), matcher(compose(first, center), valmin(apply(center,
        colorfilter(objects(branch(portrait(first(colorfilter(fgpartition(I
        ), TWO))), I, rot90(I)), T, F, T), FIVE)), first)))), toivec(add(
        THREE, height(recolor(FIVE, ofcolor(hmirror(subgrid(extract(
        colorfilter(objects(branch(portrait(first(colorfilter(fgpartition(I
        ), TWO))), I, rot90(I)), T, F, T), FIVE), matcher(compose(first,
        center), valmin(apply(center, colorfilter(objects(branch(portrait(
        first(colorfilter(fgpartition(I), TWO))), I, rot90(I)), T, F, T),
        FIVE)), first))), branch(portrait(first(colorfilter(fgpartition(I),
        TWO))), I, rot90(I)))), FIVE)))))))), shift(recolor(FIVE, ofcolor(
        hmirror(subgrid(extract(colorfilter(objects(branch(portrait(first(
        colorfilter(fgpartition(I), TWO))), I, rot90(I)), T, F, T), FIVE),
        compose(flip, matcher(compose(first, center), valmin(apply(center,
        colorfilter(objects(branch(portrait(first(colorfilter(fgpartition(I
        ), TWO))), I, rot90(I)), T, F, T), FIVE)), first)))), branch(
        portrait(first(colorfilter(fgpartition(I), TWO))), I, rot90(I)))),
        FIVE)), subtract(ulcorner(extract(colorfilter(objects(branch(
        portrait(first(colorfilter(fgpartition(I), TWO))), I, rot90(I)), T,
        F, T), FIVE), compose(flip, matcher(compose(first, center), valmin(
        apply(center, colorfilter(objects(branch(portrait(first(colorfilter
        (fgpartition(I), TWO))), I, rot90(I)), T, F, T), FIVE)), first))))),
        toivec(add(THREE, height(recolor(FIVE, ofcolor(hmirror(subgrid(
        extract(colorfilter(objects(branch(portrait(first(colorfilter(
        fgpartition(I), TWO))), I, rot90(I)), T, F, T), FIVE), compose(flip,
        matcher(compose(first, center), valmin(apply(center, colorfilter(
        objects(branch(portrait(first(colorfilter(fgpartition(I), TWO))), I,
        rot90(I)), T, F, T), FIVE)), first)))), branch(portrait(first(
        colorfilter(fgpartition(I), TWO))), I, rot90(I)))), FIVE)))))))),
        rot270(paint(paint(cover(branch(portrait(first(colorfilter(
        fgpartition(I), TWO))), I, rot90(I)), merge(colorfilter(objects(
        branch(portrait(first(colorfilter(fgpartition(I), TWO))), I, rot90(
        I)), T, F, T), FIVE))), shift(recolor(FIVE, ofcolor(hmirror(subgrid
        (extract(colorfilter(objects(branch(portrait(first(colorfilter(
        fgpartition(I), TWO))), I, rot90(I)), T, F, T), FIVE), matcher(
        compose(first, center), valmin(apply(center, colorfilter(objects(
        branch(portrait(first(colorfilter(fgpartition(I), TWO))), I, rot90(
        I)), T, F, T), FIVE)), first))), branch(portrait(first(colorfilter(
        fgpartition(I), TWO))), I, rot90(I)))), FIVE)), add(ulcorner(
        extract(colorfilter(objects(branch(portrait(first(colorfilter(
        fgpartition(I), TWO))), I, rot90(I)), T, F, T), FIVE), matcher(
        compose(first, center), valmin(apply(center, colorfilter(objects(
        branch(portrait(first(colorfilter(fgpartition(I), TWO))), I, rot90(
        I)), T, F, T), FIVE)), first)))), toivec(add(THREE, height(recolor(
        FIVE, ofcolor(hmirror(subgrid(extract(colorfilter(objects(branch(
        portrait(first(colorfilter(fgpartition(I), TWO))), I, rot90(I)), T,
        F, T), FIVE), matcher(compose(first, center), valmin(apply(center,
        colorfilter(objects(branch(portrait(first(colorfilter(fgpartition(I
        ), TWO))), I, rot90(I)), T, F, T), FIVE)), first))), branch(
        portrait(first(colorfilter(fgpartition(I), TWO))), I, rot90(I)))),
        FIVE)))))))), shift(recolor(FIVE, ofcolor(hmirror(subgrid(extract(
        colorfilter(objects(branch(portrait(first(colorfilter(fgpartition(I
        ), TWO))), I, rot90(I)), T, F, T), FIVE), compose(flip, matcher(
        compose(first, center), valmin(apply(center, colorfilter(objects(
        branch(portrait(first(colorfilter(fgpartition(I), TWO))), I, rot90(
        I)), T, F, T), FIVE)), first)))), branch(portrait(first(colorfilter
        (fgpartition(I), TWO))), I, rot90(I)))), FIVE)), subtract(ulcorner(
        extract(colorfilter(objects(branch(portrait(first(colorfilter(
        fgpartition(I), TWO))), I, rot90(I)), T, F, T), FIVE), compose(flip,
        matcher(compose(first, center), valmin(apply(center, colorfilter(
        objects(branch(portrait(first(colorfilter(fgpartition(I), TWO))), I,
        rot90(I)), T, F, T), FIVE)), first))))), toivec(add(THREE, height(
        recolor(FIVE, ofcolor(hmirror(subgrid(extract(colorfilter(objects(
        branch(portrait(first(colorfilter(fgpartition(I), TWO))), I, rot90(
        I)), T, F, T), FIVE), compose(flip, matcher(compose(first, center),
        valmin(apply(center, colorfilter(objects(branch(portrait(first(
        colorfilter(fgpartition(I), TWO))), I, rot90(I)), T, F, T), FIVE)),
        first)))), branch(portrait(first(colorfilter(fgpartition(I), TWO))),
        I, rot90(I)))), FIVE))))))))))


def solve_264363fd(I):
    return fill(paint(paint(cover(I, argmin(objects(I, F, F, T), size)),
        mapply(fork(shift, compose(asobject, fork(paint, rbind(subgrid,
        cover(I, argmin(objects(I, F, F, T), size))), compose(lbind(recolor,
        index(I, add(branch(equality(height(argmin(objects(I, F, F, T),
        size)), FIVE), UP, RIGHT), center(argmin(objects(I, F, F, T), size)
        )))), fork(combine, branch(equality(height(argmin(objects(I, F, F,
        T), size)), FIVE), compose(lbind(mapply, vfrontier), compose(rbind(
        occurrences, initset(astuple(index(I, center(argmin(objects(I, F, F,
        T), size))), ORIGIN))), rbind(subgrid, cover(I, argmin(objects(I, F,
        F, T), size))))), compose(lbind(mapply, hfrontier), compose(rbind(
        occurrences, initset(astuple(index(I, center(argmin(objects(I, F, F,
        T), size))), ORIGIN))), rbind(subgrid, cover(I, argmin(objects(I, F,
        F, T), size)))))), branch(equality(width(argmin(objects(I, F, F, T),
        size)), FIVE), compose(lbind(mapply, hfrontier), compose(rbind(
        occurrences, initset(astuple(index(I, center(argmin(objects(I, F, F,
        T), size))), ORIGIN))), rbind(subgrid, cover(I, argmin(objects(I, F,
        F, T), size))))), compose(lbind(mapply, vfrontier), compose(rbind(
        occurrences, initset(astuple(index(I, center(argmin(objects(I, F, F,
        T), size))), ORIGIN))), rbind(subgrid, cover(I, argmin(objects(I, F,
        F, T), size)))))))))), ulcorner), objects(cover(I, argmin(objects(I,
        F, F, T), size)), F, F, T))), mapply(lbind(shift, shift(normalize(
        argmin(objects(I, F, F, T), size)), invert(add(UNITY, astuple(
        equality(height(argmin(objects(I, F, F, T), size)), FIVE), equality
        (width(argmin(objects(I, F, F, T), size)), FIVE)))))), occurrences(
        cover(I, argmin(objects(I, F, F, T), size)), initset(astuple(index(
        I, center(argmin(objects(I, F, F, T), size))), ORIGIN))))),
        mostcolor(cover(I, argmin(objects(I, F, F, T), size))), ofcolor(
        cover(I, argmin(objects(I, F, F, T), size)), mostcolor(cover(I,
        argmin(objects(I, F, F, T), size)))))


def solve_7df24a62(I):
    return fill(I, ONE, mpapply(mapply, apply(chain(lbind(lbind, shift),
        rbind(shift, NEG_UNITY), compose(normalize, rbind(ofcolor, ONE))),
        combine(astuple(subgrid(ofcolor(I, ONE), I), rot90(subgrid(ofcolor(
        I, ONE), I))), astuple(rot180(subgrid(ofcolor(I, ONE), I)), rot270(
        subgrid(ofcolor(I, ONE), I))))), papply(sfilter, apply(fork(product,
        compose(lbind(rbind(interval, ONE), ZERO), chain(increment, lbind(
        subtract, height(I)), height)), compose(lbind(rbind(interval, ONE),
        ZERO), chain(increment, lbind(subtract, width(I)), width))), apply(
        normalize, apply(compose(rbind(shift, ulcorner(ofcolor(I, ONE))),
        rbind(ofcolor, FOUR)), combine(astuple(subgrid(ofcolor(I, ONE), I),
        rot90(subgrid(ofcolor(I, ONE), I))), astuple(rot180(subgrid(ofcolor
        (I, ONE), I)), rot270(subgrid(ofcolor(I, ONE), I))))))), apply(
        lbind(compose, matcher(size, ZERO)), papply(compose, apply(lbind(
        rbind, difference), apply(lbind(difference, ofcolor(I, FOUR)),
        apply(compose(rbind(shift, ulcorner(ofcolor(I, ONE))), rbind(
        ofcolor, FOUR)), combine(astuple(subgrid(ofcolor(I, ONE), I), rot90
        (subgrid(ofcolor(I, ONE), I))), astuple(rot180(subgrid(ofcolor(I,
        ONE), I)), rot270(subgrid(ofcolor(I, ONE), I))))))), apply(lbind(
        lbind, shift), apply(normalize, apply(compose(rbind(shift, ulcorner
        (ofcolor(I, ONE))), rbind(ofcolor, FOUR)), combine(astuple(subgrid(
        ofcolor(I, ONE), I), rot90(subgrid(ofcolor(I, ONE), I))), astuple(
        rot180(subgrid(ofcolor(I, ONE), I)), rot270(subgrid(ofcolor(I, ONE),
        I))))))))))))


def solve_f15e1fac(I):
    return apply_func(chain(branch(portrait(ofcolor(I, TWO)), identity,
        dmirror), branch(equality(leftmost(ofcolor(I, TWO)), ZERO),
        identity, vmirror), branch(equality(uppermost(ofcolor(apply_func(
        branch(equality(leftmost(ofcolor(I, TWO)), ZERO), identity, vmirror
        ), apply_func(branch(portrait(ofcolor(I, TWO)), identity, dmirror),
        I)), EIGHT)), ZERO), identity, hmirror)), fill(apply_func(branch(
        equality(uppermost(ofcolor(apply_func(branch(equality(leftmost(
        ofcolor(I, TWO)), ZERO), identity, vmirror), apply_func(branch(
        portrait(ofcolor(I, TWO)), identity, dmirror), I)), EIGHT)), ZERO),
        identity, hmirror), apply_func(branch(equality(leftmost(ofcolor(I,
        TWO)), ZERO), identity, vmirror), apply_func(branch(portrait(
        ofcolor(I, TWO)), identity, dmirror), I))), EIGHT, merge(papply(
        shift, apply(chain(lbind(sfilter, mapply(rbind(shoot, DOWN),
        ofcolor(apply_func(branch(equality(uppermost(ofcolor(apply_func(
        branch(equality(leftmost(ofcolor(I, TWO)), ZERO), identity, vmirror
        ), apply_func(branch(portrait(ofcolor(I, TWO)), identity, dmirror),
        I)), EIGHT)), ZERO), identity, hmirror), apply_func(branch(equality
        (leftmost(ofcolor(I, TWO)), ZERO), identity, vmirror), apply_func(
        branch(portrait(ofcolor(I, TWO)), identity, dmirror), I))), EIGHT))
        ), lbind(compose, fork(both, fork(greater, compose(first, last),
        chain(decrement, first, first)), fork(greater, chain(increment,
        last, first), compose(first, last)))), lbind(lbind, astuple)), pair
        (order(insert(ZERO, apply(first, ofcolor(apply_func(branch(equality
        (uppermost(ofcolor(apply_func(branch(equality(leftmost(ofcolor(I,
        TWO)), ZERO), identity, vmirror), apply_func(branch(portrait(
        ofcolor(I, TWO)), identity, dmirror), I)), EIGHT)), ZERO), identity,
        hmirror), apply_func(branch(equality(leftmost(ofcolor(I, TWO)),
        ZERO), identity, vmirror), apply_func(branch(portrait(ofcolor(I,
        TWO)), identity, dmirror), I))), TWO))), identity), order(apply(
        decrement, insert(height(apply_func(branch(equality(uppermost(
        ofcolor(apply_func(branch(equality(leftmost(ofcolor(I, TWO)), ZERO),
        identity, vmirror), apply_func(branch(portrait(ofcolor(I, TWO)),
        identity, dmirror), I)), EIGHT)), ZERO), identity, hmirror),
        apply_func(branch(equality(leftmost(ofcolor(I, TWO)), ZERO),
        identity, vmirror), apply_func(branch(portrait(ofcolor(I, TWO)),
        identity, dmirror), I)))), apply(first, ofcolor(apply_func(branch(
        equality(uppermost(ofcolor(apply_func(branch(equality(leftmost(
        ofcolor(I, TWO)), ZERO), identity, vmirror), apply_func(branch(
        portrait(ofcolor(I, TWO)), identity, dmirror), I)), EIGHT)), ZERO),
        identity, hmirror), apply_func(branch(equality(leftmost(ofcolor(I,
        TWO)), ZERO), identity, vmirror), apply_func(branch(portrait(
        ofcolor(I, TWO)), identity, dmirror), I))), TWO)))), identity))),
        apply(tojvec, interval(ZERO, increment(size(ofcolor(apply_func(
        branch(equality(uppermost(ofcolor(apply_func(branch(equality(
        leftmost(ofcolor(I, TWO)), ZERO), identity, vmirror), apply_func(
        branch(portrait(ofcolor(I, TWO)), identity, dmirror), I)), EIGHT)),
        ZERO), identity, hmirror), apply_func(branch(equality(leftmost(
        ofcolor(I, TWO)), ZERO), identity, vmirror), apply_func(branch(
        portrait(ofcolor(I, TWO)), identity, dmirror), I))), TWO))), ONE))))))


def solve_234bbc79(I):
    return paint(canvas(ZERO, astuple(THREE, decrement(width(first(
        apply_func(power(fork(astuple, fork(combine, first, fork(shift,
        compose(first, last), compose(lbind(add, RIGHT), fork(subtract,
        compose(compose(last, fork(argmin, fork(sfilter, identity, compose(
        lbind(matcher, compose(last, last)), rightmost)), chain(lbind(rbind
        (chain, compose(dneighbors, last)), size), lbind(rbind,
        intersection), toindices))), first), chain(compose(last, fork(
        argmin, fork(sfilter, identity, compose(lbind(matcher, compose(last,
        last)), leftmost)), chain(lbind(rbind(chain, compose(dneighbors,
        last)), size), lbind(rbind, intersection), toindices))), first,
        last))))), fork(remove, compose(first, last), last)), size(objects(
        I, F, F, T))), astuple(initset(astuple(ZERO, DOWN_LEFT)), order(
        apply(fork(recolor, compose(rbind(other, FIVE), palette), identity),
        objects(I, F, F, T)), leftmost)))))))), first(apply_func(power(fork
        (astuple, fork(combine, first, fork(shift, compose(first, last),
        compose(lbind(add, RIGHT), fork(subtract, compose(compose(last,
        fork(argmin, fork(sfilter, identity, compose(lbind(matcher, compose
        (last, last)), rightmost)), chain(lbind(rbind(chain, compose(
        dneighbors, last)), size), lbind(rbind, intersection), toindices))),
        first), chain(compose(last, fork(argmin, fork(sfilter, identity,
        compose(lbind(matcher, compose(last, last)), leftmost)), chain(
        lbind(rbind(chain, compose(dneighbors, last)), size), lbind(rbind,
        intersection), toindices))), first, last))))), fork(remove, compose
        (first, last), last)), size(objects(I, F, F, T))), astuple(initset(
        astuple(ZERO, DOWN_LEFT)), order(apply(fork(recolor, compose(rbind(
        other, FIVE), palette), identity), objects(I, F, F, T)), leftmost)))))


def solve_22233c11(I):
    return fill(I, EIGHT, mapply(fork(difference, compose(toindices, fork(
        shift, compose(rbind(upscale, TWO), vmirror), chain(invert, halve,
        shape))), compose(lbind(mapply, fork(combine, hfrontier, vfrontier)
        ), toindices)), objects(I, T, T, T)))


def solve_2dd70a9a(I):
    return replace(underfill(fill(cover(underfill(I, ONE, shoot(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))), subtract(astuple(apply_func(branch
        (both(vline(ofcolor(I, THREE)), greater(apply_func(branch(vline(
        ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))), other(ofcolor(I, THREE), astuple(apply_func(
        branch(both(vline(ofcolor(I, THREE)), greater(apply_func(branch(
        vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))))))), merge(difference(colorfilter(objects(
        underfill(I, ONE, shoot(astuple(apply_func(branch(both(vline(
        ofcolor(I, THREE)), greater(apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, TWO)), apply_func(branch
        (vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, THREE)
        ))), lowermost, uppermost), ofcolor(I, THREE)), apply_func(branch(
        vline(ofcolor(I, THREE)), leftmost, rightmost), ofcolor(I, THREE))),
        subtract(astuple(apply_func(branch(both(vline(ofcolor(I, THREE)),
        greater(apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, THREE)))), lowermost,
        uppermost), ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I,
        THREE)), leftmost, rightmost), ofcolor(I, THREE))), other(ofcolor(I,
        THREE), astuple(apply_func(branch(both(vline(ofcolor(I, THREE)),
        greater(apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, THREE)))), lowermost,
        uppermost), ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I,
        THREE)), leftmost, rightmost), ofcolor(I, THREE))))))), T, F, F),
        ONE), sfilter(colorfilter(objects(underfill(I, ONE, shoot(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))), subtract(astuple(apply_func(branch
        (both(vline(ofcolor(I, THREE)), greater(apply_func(branch(vline(
        ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))), other(ofcolor(I, THREE), astuple(apply_func(
        branch(both(vline(ofcolor(I, THREE)), greater(apply_func(branch(
        vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))))))), T, F, F), ONE), rbind(adjacent, ofcolor(I,
        THREE)))))), ONE, connect(argmax(ofcolor(cover(underfill(I, ONE,
        shoot(astuple(apply_func(branch(both(vline(ofcolor(I, THREE)),
        greater(apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, THREE)))), lowermost,
        uppermost), ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I,
        THREE)), leftmost, rightmost), ofcolor(I, THREE))), subtract(
        astuple(apply_func(branch(both(vline(ofcolor(I, THREE)), greater(
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I, THREE)),
        uppermost, rightmost), ofcolor(I, THREE)))), lowermost, uppermost),
        ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I, THREE)),
        leftmost, rightmost), ofcolor(I, THREE))), other(ofcolor(I, THREE),
        astuple(apply_func(branch(both(vline(ofcolor(I, THREE)), greater(
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I, THREE)),
        uppermost, rightmost), ofcolor(I, THREE)))), lowermost, uppermost),
        ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I, THREE)),
        leftmost, rightmost), ofcolor(I, THREE))))))), merge(difference(
        colorfilter(objects(underfill(I, ONE, shoot(astuple(apply_func(
        branch(both(vline(ofcolor(I, THREE)), greater(apply_func(branch(
        vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))), subtract(astuple(apply_func(branch(both(vline(
        ofcolor(I, THREE)), greater(apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, TWO)), apply_func(branch
        (vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, THREE)
        ))), lowermost, uppermost), ofcolor(I, THREE)), apply_func(branch(
        vline(ofcolor(I, THREE)), leftmost, rightmost), ofcolor(I, THREE))),
        other(ofcolor(I, THREE), astuple(apply_func(branch(both(vline(
        ofcolor(I, THREE)), greater(apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, TWO)), apply_func(branch
        (vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, THREE)
        ))), lowermost, uppermost), ofcolor(I, THREE)), apply_func(branch(
        vline(ofcolor(I, THREE)), leftmost, rightmost), ofcolor(I, THREE)))
        )))), T, F, F), ONE), sfilter(colorfilter(objects(underfill(I, ONE,
        shoot(astuple(apply_func(branch(both(vline(ofcolor(I, THREE)),
        greater(apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, THREE)))), lowermost,
        uppermost), ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I,
        THREE)), leftmost, rightmost), ofcolor(I, THREE))), subtract(
        astuple(apply_func(branch(both(vline(ofcolor(I, THREE)), greater(
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I, THREE)),
        uppermost, rightmost), ofcolor(I, THREE)))), lowermost, uppermost),
        ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I, THREE)),
        leftmost, rightmost), ofcolor(I, THREE))), other(ofcolor(I, THREE),
        astuple(apply_func(branch(both(vline(ofcolor(I, THREE)), greater(
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I, THREE)),
        uppermost, rightmost), ofcolor(I, THREE)))), lowermost, uppermost),
        ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I, THREE)),
        leftmost, rightmost), ofcolor(I, THREE))))))), T, F, F), ONE),
        rbind(adjacent, ofcolor(I, THREE)))))), ONE), compose(rbind(
        manhattan, initset(astuple(apply_func(branch(both(vline(ofcolor(I,
        THREE)), greater(apply_func(branch(vline(ofcolor(I, THREE)),
        uppermost, rightmost), ofcolor(I, TWO)), apply_func(branch(vline(
        ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, THREE)))),
        lowermost, uppermost), ofcolor(I, THREE)), apply_func(branch(vline(
        ofcolor(I, THREE)), leftmost, rightmost), ofcolor(I, THREE))))),
        initset)), add(argmax(ofcolor(cover(underfill(I, ONE, shoot(astuple
        (apply_func(branch(both(vline(ofcolor(I, THREE)), greater(
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I, THREE)),
        uppermost, rightmost), ofcolor(I, THREE)))), lowermost, uppermost),
        ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I, THREE)),
        leftmost, rightmost), ofcolor(I, THREE))), subtract(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))), other(ofcolor(I, THREE), astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))))))), merge(difference(colorfilter(
        objects(underfill(I, ONE, shoot(astuple(apply_func(branch(both(
        vline(ofcolor(I, THREE)), greater(apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, TWO)), apply_func(branch
        (vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, THREE)
        ))), lowermost, uppermost), ofcolor(I, THREE)), apply_func(branch(
        vline(ofcolor(I, THREE)), leftmost, rightmost), ofcolor(I, THREE))),
        subtract(astuple(apply_func(branch(both(vline(ofcolor(I, THREE)),
        greater(apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, THREE)))), lowermost,
        uppermost), ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I,
        THREE)), leftmost, rightmost), ofcolor(I, THREE))), other(ofcolor(I,
        THREE), astuple(apply_func(branch(both(vline(ofcolor(I, THREE)),
        greater(apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, THREE)))), lowermost,
        uppermost), ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I,
        THREE)), leftmost, rightmost), ofcolor(I, THREE))))))), T, F, F),
        ONE), sfilter(colorfilter(objects(underfill(I, ONE, shoot(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))), subtract(astuple(apply_func(branch
        (both(vline(ofcolor(I, THREE)), greater(apply_func(branch(vline(
        ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))), other(ofcolor(I, THREE), astuple(apply_func(
        branch(both(vline(ofcolor(I, THREE)), greater(apply_func(branch(
        vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))))))), T, F, F), ONE), rbind(adjacent, ofcolor(I,
        THREE)))))), ONE), compose(rbind(manhattan, initset(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))))), initset)), crement(gravitate(
        initset(argmax(ofcolor(cover(underfill(I, ONE, shoot(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))), subtract(astuple(apply_func(branch
        (both(vline(ofcolor(I, THREE)), greater(apply_func(branch(vline(
        ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))), other(ofcolor(I, THREE), astuple(apply_func(
        branch(both(vline(ofcolor(I, THREE)), greater(apply_func(branch(
        vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))))))), merge(difference(colorfilter(objects(
        underfill(I, ONE, shoot(astuple(apply_func(branch(both(vline(
        ofcolor(I, THREE)), greater(apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, TWO)), apply_func(branch
        (vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, THREE)
        ))), lowermost, uppermost), ofcolor(I, THREE)), apply_func(branch(
        vline(ofcolor(I, THREE)), leftmost, rightmost), ofcolor(I, THREE))),
        subtract(astuple(apply_func(branch(both(vline(ofcolor(I, THREE)),
        greater(apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, THREE)))), lowermost,
        uppermost), ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I,
        THREE)), leftmost, rightmost), ofcolor(I, THREE))), other(ofcolor(I,
        THREE), astuple(apply_func(branch(both(vline(ofcolor(I, THREE)),
        greater(apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, THREE)))), lowermost,
        uppermost), ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I,
        THREE)), leftmost, rightmost), ofcolor(I, THREE))))))), T, F, F),
        ONE), sfilter(colorfilter(objects(underfill(I, ONE, shoot(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))), subtract(astuple(apply_func(branch
        (both(vline(ofcolor(I, THREE)), greater(apply_func(branch(vline(
        ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))), other(ofcolor(I, THREE), astuple(apply_func(
        branch(both(vline(ofcolor(I, THREE)), greater(apply_func(branch(
        vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))))))), T, F, F), ONE), rbind(adjacent, ofcolor(I,
        THREE)))))), ONE), compose(rbind(manhattan, initset(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))))), initset))), branch(vline(ofcolor
        (I, TWO)), combine(shoot(center(ofcolor(I, TWO)), DOWN), shoot(
        center(ofcolor(I, TWO)), UP)), combine(shoot(center(ofcolor(I, TWO)
        ), LEFT), shoot(center(ofcolor(I, TWO)), RIGHT)))))))), ONE,
        connect(add(argmax(ofcolor(cover(underfill(I, ONE, shoot(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))), subtract(astuple(apply_func(branch
        (both(vline(ofcolor(I, THREE)), greater(apply_func(branch(vline(
        ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))), other(ofcolor(I, THREE), astuple(apply_func(
        branch(both(vline(ofcolor(I, THREE)), greater(apply_func(branch(
        vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))))))), merge(difference(colorfilter(objects(
        underfill(I, ONE, shoot(astuple(apply_func(branch(both(vline(
        ofcolor(I, THREE)), greater(apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, TWO)), apply_func(branch
        (vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, THREE)
        ))), lowermost, uppermost), ofcolor(I, THREE)), apply_func(branch(
        vline(ofcolor(I, THREE)), leftmost, rightmost), ofcolor(I, THREE))),
        subtract(astuple(apply_func(branch(both(vline(ofcolor(I, THREE)),
        greater(apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, THREE)))), lowermost,
        uppermost), ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I,
        THREE)), leftmost, rightmost), ofcolor(I, THREE))), other(ofcolor(I,
        THREE), astuple(apply_func(branch(both(vline(ofcolor(I, THREE)),
        greater(apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, THREE)))), lowermost,
        uppermost), ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I,
        THREE)), leftmost, rightmost), ofcolor(I, THREE))))))), T, F, F),
        ONE), sfilter(colorfilter(objects(underfill(I, ONE, shoot(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))), subtract(astuple(apply_func(branch
        (both(vline(ofcolor(I, THREE)), greater(apply_func(branch(vline(
        ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))), other(ofcolor(I, THREE), astuple(apply_func(
        branch(both(vline(ofcolor(I, THREE)), greater(apply_func(branch(
        vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))))))), T, F, F), ONE), rbind(adjacent, ofcolor(I,
        THREE)))))), ONE), compose(rbind(manhattan, initset(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))))), initset)), crement(gravitate(
        initset(argmax(ofcolor(cover(underfill(I, ONE, shoot(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))), subtract(astuple(apply_func(branch
        (both(vline(ofcolor(I, THREE)), greater(apply_func(branch(vline(
        ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))), other(ofcolor(I, THREE), astuple(apply_func(
        branch(both(vline(ofcolor(I, THREE)), greater(apply_func(branch(
        vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))))))), merge(difference(colorfilter(objects(
        underfill(I, ONE, shoot(astuple(apply_func(branch(both(vline(
        ofcolor(I, THREE)), greater(apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, TWO)), apply_func(branch
        (vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, THREE)
        ))), lowermost, uppermost), ofcolor(I, THREE)), apply_func(branch(
        vline(ofcolor(I, THREE)), leftmost, rightmost), ofcolor(I, THREE))),
        subtract(astuple(apply_func(branch(both(vline(ofcolor(I, THREE)),
        greater(apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, THREE)))), lowermost,
        uppermost), ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I,
        THREE)), leftmost, rightmost), ofcolor(I, THREE))), other(ofcolor(I,
        THREE), astuple(apply_func(branch(both(vline(ofcolor(I, THREE)),
        greater(apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, TWO)), apply_func(branch(vline(ofcolor(I,
        THREE)), uppermost, rightmost), ofcolor(I, THREE)))), lowermost,
        uppermost), ofcolor(I, THREE)), apply_func(branch(vline(ofcolor(I,
        THREE)), leftmost, rightmost), ofcolor(I, THREE))))))), T, F, F),
        ONE), sfilter(colorfilter(objects(underfill(I, ONE, shoot(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))), subtract(astuple(apply_func(branch
        (both(vline(ofcolor(I, THREE)), greater(apply_func(branch(vline(
        ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))), other(ofcolor(I, THREE), astuple(apply_func(
        branch(both(vline(ofcolor(I, THREE)), greater(apply_func(branch(
        vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I, TWO)),
        apply_func(branch(vline(ofcolor(I, THREE)), uppermost, rightmost),
        ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I, THREE)),
        apply_func(branch(vline(ofcolor(I, THREE)), leftmost, rightmost),
        ofcolor(I, THREE))))))), T, F, F), ONE), rbind(adjacent, ofcolor(I,
        THREE)))))), ONE), compose(rbind(manhattan, initset(astuple(
        apply_func(branch(both(vline(ofcolor(I, THREE)), greater(apply_func
        (branch(vline(ofcolor(I, THREE)), uppermost, rightmost), ofcolor(I,
        TWO)), apply_func(branch(vline(ofcolor(I, THREE)), uppermost,
        rightmost), ofcolor(I, THREE)))), lowermost, uppermost), ofcolor(I,
        THREE)), apply_func(branch(vline(ofcolor(I, THREE)), leftmost,
        rightmost), ofcolor(I, THREE))))), initset))), branch(vline(ofcolor
        (I, TWO)), combine(shoot(center(ofcolor(I, TWO)), DOWN), shoot(
        center(ofcolor(I, TWO)), UP)), combine(shoot(center(ofcolor(I, TWO)
        ), LEFT), shoot(center(ofcolor(I, TWO)), RIGHT)))))), center(
        ofcolor(I, TWO)))), ONE, THREE)


def solve_a64e4611(I):
    return fill(fill(I, THREE, sfilter(asindices(I), matcher(chain(rbind(
        colorcount, THREE), rbind(toobject, fill(fill(fill(I, THREE,
        apply_func(fork(mapply, chain(lbind(lbind, shift), compose(asobject,
        lbind(canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, multiply(
        TWO, SIX), ONE), I))), THREE, apply_func(fork(mapply, chain(lbind(
        lbind, shift), compose(asobject, lbind(canvas, ZERO)), fork(argmax,
        compose(fork(product, identity, identity), first), compose(chain(
        lbind(rbind(fork, fork(multiply, first, last)), multiply), rbind(
        lbind(chain, compose(positive, size)), compose(asobject, lbind(
        canvas, ZERO))), lbind(lbind, occurrences)), last))), fork(
        occurrences, last, compose(compose(asobject, lbind(canvas, ZERO)),
        fork(argmax, compose(fork(product, identity, identity), first),
        compose(chain(lbind(rbind(fork, fork(multiply, first, last)),
        multiply), rbind(lbind(chain, compose(positive, size)), compose(
        asobject, lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))
        ))), astuple(interval(THREE, TEN, ONE), fill(I, THREE, apply_func(
        fork(mapply, chain(lbind(lbind, shift), compose(asobject, lbind(
        canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, multiply(
        TWO, SIX), ONE), I)))))), THREE, apply_func(fork(mapply, chain(
        lbind(lbind, shift), compose(asobject, lbind(canvas, ZERO)), fork(
        argmax, compose(fork(product, identity, identity), first), compose(
        chain(lbind(rbind(fork, fork(multiply, first, last)), multiply),
        rbind(lbind(chain, compose(positive, size)), compose(asobject,
        lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))), fork(
        occurrences, last, compose(compose(asobject, lbind(canvas, ZERO)),
        fork(argmax, compose(fork(product, identity, identity), first),
        compose(chain(lbind(rbind(fork, fork(multiply, first, last)),
        multiply), rbind(lbind(chain, compose(positive, size)), compose(
        asobject, lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))
        ))), astuple(interval(THREE, TEN, ONE), fill(fill(I, THREE,
        apply_func(fork(mapply, chain(lbind(lbind, shift), compose(asobject,
        lbind(canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, multiply(
        TWO, SIX), ONE), I))), THREE, apply_func(fork(mapply, chain(lbind(
        lbind, shift), compose(asobject, lbind(canvas, ZERO)), fork(argmax,
        compose(fork(product, identity, identity), first), compose(chain(
        lbind(rbind(fork, fork(multiply, first, last)), multiply), rbind(
        lbind(chain, compose(positive, size)), compose(asobject, lbind(
        canvas, ZERO))), lbind(lbind, occurrences)), last))), fork(
        occurrences, last, compose(compose(asobject, lbind(canvas, ZERO)),
        fork(argmax, compose(fork(product, identity, identity), first),
        compose(chain(lbind(rbind(fork, fork(multiply, first, last)),
        multiply), rbind(lbind(chain, compose(positive, size)), compose(
        asobject, lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))
        ))), astuple(interval(THREE, TEN, ONE), fill(I, THREE, apply_func(
        fork(mapply, chain(lbind(lbind, shift), compose(asobject, lbind(
        canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, multiply(
        TWO, SIX), ONE), I)))))))))), neighbors), EIGHT))), THREE, sfilter(
        ofcolor(fill(I, THREE, sfilter(asindices(I), matcher(chain(rbind(
        colorcount, THREE), rbind(toobject, fill(fill(fill(I, THREE,
        apply_func(fork(mapply, chain(lbind(lbind, shift), compose(asobject,
        lbind(canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, multiply(
        TWO, SIX), ONE), I))), THREE, apply_func(fork(mapply, chain(lbind(
        lbind, shift), compose(asobject, lbind(canvas, ZERO)), fork(argmax,
        compose(fork(product, identity, identity), first), compose(chain(
        lbind(rbind(fork, fork(multiply, first, last)), multiply), rbind(
        lbind(chain, compose(positive, size)), compose(asobject, lbind(
        canvas, ZERO))), lbind(lbind, occurrences)), last))), fork(
        occurrences, last, compose(compose(asobject, lbind(canvas, ZERO)),
        fork(argmax, compose(fork(product, identity, identity), first),
        compose(chain(lbind(rbind(fork, fork(multiply, first, last)),
        multiply), rbind(lbind(chain, compose(positive, size)), compose(
        asobject, lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))
        ))), astuple(interval(THREE, TEN, ONE), fill(I, THREE, apply_func(
        fork(mapply, chain(lbind(lbind, shift), compose(asobject, lbind(
        canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, multiply(
        TWO, SIX), ONE), I)))))), THREE, apply_func(fork(mapply, chain(
        lbind(lbind, shift), compose(asobject, lbind(canvas, ZERO)), fork(
        argmax, compose(fork(product, identity, identity), first), compose(
        chain(lbind(rbind(fork, fork(multiply, first, last)), multiply),
        rbind(lbind(chain, compose(positive, size)), compose(asobject,
        lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))), fork(
        occurrences, last, compose(compose(asobject, lbind(canvas, ZERO)),
        fork(argmax, compose(fork(product, identity, identity), first),
        compose(chain(lbind(rbind(fork, fork(multiply, first, last)),
        multiply), rbind(lbind(chain, compose(positive, size)), compose(
        asobject, lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))
        ))), astuple(interval(THREE, TEN, ONE), fill(fill(I, THREE,
        apply_func(fork(mapply, chain(lbind(lbind, shift), compose(asobject,
        lbind(canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, multiply(
        TWO, SIX), ONE), I))), THREE, apply_func(fork(mapply, chain(lbind(
        lbind, shift), compose(asobject, lbind(canvas, ZERO)), fork(argmax,
        compose(fork(product, identity, identity), first), compose(chain(
        lbind(rbind(fork, fork(multiply, first, last)), multiply), rbind(
        lbind(chain, compose(positive, size)), compose(asobject, lbind(
        canvas, ZERO))), lbind(lbind, occurrences)), last))), fork(
        occurrences, last, compose(compose(asobject, lbind(canvas, ZERO)),
        fork(argmax, compose(fork(product, identity, identity), first),
        compose(chain(lbind(rbind(fork, fork(multiply, first, last)),
        multiply), rbind(lbind(chain, compose(positive, size)), compose(
        asobject, lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))
        ))), astuple(interval(THREE, TEN, ONE), fill(I, THREE, apply_func(
        fork(mapply, chain(lbind(lbind, shift), compose(asobject, lbind(
        canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, multiply(
        TWO, SIX), ONE), I)))))))))), neighbors), EIGHT))), ZERO), fork(
        both, compose(chain(lbind(contained, THREE), palette, rbind(
        toobject, fill(I, THREE, sfilter(asindices(I), matcher(chain(rbind(
        colorcount, THREE), rbind(toobject, fill(fill(fill(I, THREE,
        apply_func(fork(mapply, chain(lbind(lbind, shift), compose(asobject,
        lbind(canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, multiply(
        TWO, SIX), ONE), I))), THREE, apply_func(fork(mapply, chain(lbind(
        lbind, shift), compose(asobject, lbind(canvas, ZERO)), fork(argmax,
        compose(fork(product, identity, identity), first), compose(chain(
        lbind(rbind(fork, fork(multiply, first, last)), multiply), rbind(
        lbind(chain, compose(positive, size)), compose(asobject, lbind(
        canvas, ZERO))), lbind(lbind, occurrences)), last))), fork(
        occurrences, last, compose(compose(asobject, lbind(canvas, ZERO)),
        fork(argmax, compose(fork(product, identity, identity), first),
        compose(chain(lbind(rbind(fork, fork(multiply, first, last)),
        multiply), rbind(lbind(chain, compose(positive, size)), compose(
        asobject, lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))
        ))), astuple(interval(THREE, TEN, ONE), fill(I, THREE, apply_func(
        fork(mapply, chain(lbind(lbind, shift), compose(asobject, lbind(
        canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, multiply(
        TWO, SIX), ONE), I)))))), THREE, apply_func(fork(mapply, chain(
        lbind(lbind, shift), compose(asobject, lbind(canvas, ZERO)), fork(
        argmax, compose(fork(product, identity, identity), first), compose(
        chain(lbind(rbind(fork, fork(multiply, first, last)), multiply),
        rbind(lbind(chain, compose(positive, size)), compose(asobject,
        lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))), fork(
        occurrences, last, compose(compose(asobject, lbind(canvas, ZERO)),
        fork(argmax, compose(fork(product, identity, identity), first),
        compose(chain(lbind(rbind(fork, fork(multiply, first, last)),
        multiply), rbind(lbind(chain, compose(positive, size)), compose(
        asobject, lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))
        ))), astuple(interval(THREE, TEN, ONE), fill(fill(I, THREE,
        apply_func(fork(mapply, chain(lbind(lbind, shift), compose(asobject,
        lbind(canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, multiply(
        TWO, SIX), ONE), I))), THREE, apply_func(fork(mapply, chain(lbind(
        lbind, shift), compose(asobject, lbind(canvas, ZERO)), fork(argmax,
        compose(fork(product, identity, identity), first), compose(chain(
        lbind(rbind(fork, fork(multiply, first, last)), multiply), rbind(
        lbind(chain, compose(positive, size)), compose(asobject, lbind(
        canvas, ZERO))), lbind(lbind, occurrences)), last))), fork(
        occurrences, last, compose(compose(asobject, lbind(canvas, ZERO)),
        fork(argmax, compose(fork(product, identity, identity), first),
        compose(chain(lbind(rbind(fork, fork(multiply, first, last)),
        multiply), rbind(lbind(chain, compose(positive, size)), compose(
        asobject, lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))
        ))), astuple(interval(THREE, TEN, ONE), fill(I, THREE, apply_func(
        fork(mapply, chain(lbind(lbind, shift), compose(asobject, lbind(
        canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, multiply(
        TWO, SIX), ONE), I)))))))))), neighbors), EIGHT))))), dneighbors),
        compose(rbind(bordering, fill(I, THREE, sfilter(asindices(I),
        matcher(chain(rbind(colorcount, THREE), rbind(toobject, fill(fill(
        fill(I, THREE, apply_func(fork(mapply, chain(lbind(lbind, shift),
        compose(asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(
        product, identity, identity), first), compose(chain(lbind(rbind(
        fork, fork(multiply, first, last)), multiply), rbind(lbind(chain,
        compose(positive, size)), compose(asobject, lbind(canvas, ZERO))),
        lbind(lbind, occurrences)), last))), fork(occurrences, last,
        compose(compose(asobject, lbind(canvas, ZERO)), fork(argmax,
        compose(fork(product, identity, identity), first), compose(chain(
        lbind(rbind(fork, fork(multiply, first, last)), multiply), rbind(
        lbind(chain, compose(positive, size)), compose(asobject, lbind(
        canvas, ZERO))), lbind(lbind, occurrences)), last))))), astuple(
        interval(THREE, multiply(TWO, SIX), ONE), I))), THREE, apply_func(
        fork(mapply, chain(lbind(lbind, shift), compose(asobject, lbind(
        canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, TEN, ONE),
        fill(I, THREE, apply_func(fork(mapply, chain(lbind(lbind, shift),
        compose(asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(
        product, identity, identity), first), compose(chain(lbind(rbind(
        fork, fork(multiply, first, last)), multiply), rbind(lbind(chain,
        compose(positive, size)), compose(asobject, lbind(canvas, ZERO))),
        lbind(lbind, occurrences)), last))), fork(occurrences, last,
        compose(compose(asobject, lbind(canvas, ZERO)), fork(argmax,
        compose(fork(product, identity, identity), first), compose(chain(
        lbind(rbind(fork, fork(multiply, first, last)), multiply), rbind(
        lbind(chain, compose(positive, size)), compose(asobject, lbind(
        canvas, ZERO))), lbind(lbind, occurrences)), last))))), astuple(
        interval(THREE, multiply(TWO, SIX), ONE), I)))))), THREE,
        apply_func(fork(mapply, chain(lbind(lbind, shift), compose(asobject,
        lbind(canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, TEN, ONE),
        fill(fill(I, THREE, apply_func(fork(mapply, chain(lbind(lbind,
        shift), compose(asobject, lbind(canvas, ZERO)), fork(argmax,
        compose(fork(product, identity, identity), first), compose(chain(
        lbind(rbind(fork, fork(multiply, first, last)), multiply), rbind(
        lbind(chain, compose(positive, size)), compose(asobject, lbind(
        canvas, ZERO))), lbind(lbind, occurrences)), last))), fork(
        occurrences, last, compose(compose(asobject, lbind(canvas, ZERO)),
        fork(argmax, compose(fork(product, identity, identity), first),
        compose(chain(lbind(rbind(fork, fork(multiply, first, last)),
        multiply), rbind(lbind(chain, compose(positive, size)), compose(
        asobject, lbind(canvas, ZERO))), lbind(lbind, occurrences)), last))
        ))), astuple(interval(THREE, multiply(TWO, SIX), ONE), I))), THREE,
        apply_func(fork(mapply, chain(lbind(lbind, shift), compose(asobject,
        lbind(canvas, ZERO)), fork(argmax, compose(fork(product, identity,
        identity), first), compose(chain(lbind(rbind(fork, fork(multiply,
        first, last)), multiply), rbind(lbind(chain, compose(positive, size
        )), compose(asobject, lbind(canvas, ZERO))), lbind(lbind,
        occurrences)), last))), fork(occurrences, last, compose(compose(
        asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(product,
        identity, identity), first), compose(chain(lbind(rbind(fork, fork(
        multiply, first, last)), multiply), rbind(lbind(chain, compose(
        positive, size)), compose(asobject, lbind(canvas, ZERO))), lbind(
        lbind, occurrences)), last))))), astuple(interval(THREE, TEN, ONE),
        fill(I, THREE, apply_func(fork(mapply, chain(lbind(lbind, shift),
        compose(asobject, lbind(canvas, ZERO)), fork(argmax, compose(fork(
        product, identity, identity), first), compose(chain(lbind(rbind(
        fork, fork(multiply, first, last)), multiply), rbind(lbind(chain,
        compose(positive, size)), compose(asobject, lbind(canvas, ZERO))),
        lbind(lbind, occurrences)), last))), fork(occurrences, last,
        compose(compose(asobject, lbind(canvas, ZERO)), fork(argmax,
        compose(fork(product, identity, identity), first), compose(chain(
        lbind(rbind(fork, fork(multiply, first, last)), multiply), rbind(
        lbind(chain, compose(positive, size)), compose(asobject, lbind(
        canvas, ZERO))), lbind(lbind, occurrences)), last))))), astuple(
        interval(THREE, multiply(TWO, SIX), ONE), I)))))))))), neighbors),
        EIGHT)))), initset))))


def solve_7837ac64(I):
    return downscale(apply_func(power(compose(dmirror, chain(lbind(apply,
        first), rbind(sfilter, chain(flip, rbind(contained, interval(ZERO,
        height(subgrid(merge(remove(argmax(fgpartition(I), size),
        fgpartition(I))), I)), increment(height(first(colorfilter(objects(
        subgrid(merge(remove(argmax(fgpartition(I), size), fgpartition(I))),
        I), T, F, F), ZERO)))))), last)), rbind(pair, interval(ZERO, height
        (subgrid(merge(remove(argmax(fgpartition(I), size), fgpartition(I))
        ), I)), ONE)))), TWO), paint(subgrid(merge(remove(argmax(
        fgpartition(I), size), fgpartition(I))), I), mapply(fork(recolor,
        compose(color, chain(rbind(toobject, subgrid(merge(remove(argmax(
        fgpartition(I), size), fgpartition(I))), I)), corners, outbox)),
        identity), sfilter(colorfilter(objects(subgrid(merge(remove(argmax(
        fgpartition(I), size), fgpartition(I))), I), T, F, F), ZERO), fork(
        both, compose(flip, chain(lbind(contained, apply_func(chain(color,
        merge, frontiers), I)), palette, chain(rbind(toobject, subgrid(
        merge(remove(argmax(fgpartition(I), size), fgpartition(I))), I)),
        corners, outbox))), matcher(compose(numcolors, chain(rbind(toobject,
        subgrid(merge(remove(argmax(fgpartition(I), size), fgpartition(I))),
        I)), corners, outbox)), ONE)))))), height(first(colorfilter(objects
        (subgrid(merge(remove(argmax(fgpartition(I), size), fgpartition(I))
        ), I), T, F, F), ZERO))))


def solve_a8c38be5(I):
    return paint(canvas(FIVE, astuple(NINE, NINE)), mapply(fork(shift,
        identity, compose(chain(ulcorner, lbind(extract, apply(toindices,
        objects(fill(canvas(FIVE, astuple(NINE, NINE)), ONE, combine(
        difference(box(asindices(canvas(FIVE, astuple(NINE, NINE)))),
        mapply(chain(outbox, outbox, initset), corners(asindices(canvas(
        FIVE, astuple(NINE, NINE)))))), sfilter(inbox(box(asindices(canvas(
        FIVE, astuple(NINE, NINE))))), compose(lbind(contained, ZERO),
        rbind(subtract, center(asindices(canvas(FIVE, astuple(NINE, NINE)))
        )))))), T, F, T))), lbind(matcher, normalize)), toindices)), apply(
        normalize, objects(replace(I, FIVE, ZERO), T, F, T))))


def solve_b775ac94(I):
    return paint(paint(paint(I, mapply(fork(recolor, chain(lbind(index, I),
        first, fork(intersection, apply_func(lbind(compose, toindices),
        fork(combine, fork(insert, fork(extract, fork(sfilter, identity,
        chain(rbind(compose, first), lbind(rbind, equality), mostcolor)),
        chain(rbind(compose, initset), lbind(rbind, adjacent), fork(
        difference, identity, fork(sfilter, identity, chain(rbind(compose,
        first), lbind(rbind, equality), mostcolor))))), fork(difference,
        identity, fork(sfilter, identity, chain(rbind(compose, first),
        lbind(rbind, equality), mostcolor)))), chain(lbind(recolor, ZERO),
        delta, fork(insert, fork(extract, fork(sfilter, identity, chain(
        rbind(compose, first), lbind(rbind, equality), mostcolor)), chain(
        rbind(compose, initset), lbind(rbind, adjacent), fork(difference,
        identity, fork(sfilter, identity, chain(rbind(compose, first),
        lbind(rbind, equality), mostcolor))))), fork(difference, identity,
        fork(sfilter, identity, chain(rbind(compose, first), lbind(rbind,
        equality), mostcolor))))))), apply_func(lbind(compose, toindices),
        fork(shift, apply_func(lbind(compose, fork(sfilter, identity, chain
        (rbind(compose, first), lbind(rbind, equality), mostcolor))), fork(
        shift, hmirror, fork(multiply, shape, chain(toivec, first, fork(
        position, fork(sfilter, identity, chain(rbind(compose, first),
        lbind(rbind, equality), mostcolor)), fork(difference, identity,
        fork(sfilter, identity, chain(rbind(compose, first), lbind(rbind,
        equality), mostcolor)))))))), apply_func(lbind(compose, compose(
        crement, invert)), chain(toivec, first, fork(position, fork(sfilter,
        identity, chain(rbind(compose, first), lbind(rbind, equality),
        mostcolor)), fork(difference, identity, fork(sfilter, identity,
        chain(rbind(compose, first), lbind(rbind, equality), mostcolor)))))
        ))))), fork(shift, apply_func(lbind(compose, fork(sfilter, identity,
        chain(rbind(compose, first), lbind(rbind, equality), mostcolor))),
        fork(shift, hmirror, fork(multiply, shape, chain(toivec, first,
        fork(position, fork(sfilter, identity, chain(rbind(compose, first),
        lbind(rbind, equality), mostcolor)), fork(difference, identity,
        fork(sfilter, identity, chain(rbind(compose, first), lbind(rbind,
        equality), mostcolor)))))))), apply_func(lbind(compose, compose(
        crement, invert)), chain(toivec, first, fork(position, fork(sfilter,
        identity, chain(rbind(compose, first), lbind(rbind, equality),
        mostcolor)), fork(difference, identity, fork(sfilter, identity,
        chain(rbind(compose, first), lbind(rbind, equality), mostcolor)))))
        ))), objects(I, F, T, T))), mapply(fork(recolor, chain(lbind(index,
        I), first, fork(intersection, apply_func(lbind(compose, toindices),
        fork(combine, fork(insert, fork(extract, fork(sfilter, identity,
        chain(rbind(compose, first), lbind(rbind, equality), mostcolor)),
        chain(rbind(compose, initset), lbind(rbind, adjacent), fork(
        difference, identity, fork(sfilter, identity, chain(rbind(compose,
        first), lbind(rbind, equality), mostcolor))))), fork(difference,
        identity, fork(sfilter, identity, chain(rbind(compose, first),
        lbind(rbind, equality), mostcolor)))), chain(lbind(recolor, ZERO),
        delta, fork(insert, fork(extract, fork(sfilter, identity, chain(
        rbind(compose, first), lbind(rbind, equality), mostcolor)), chain(
        rbind(compose, initset), lbind(rbind, adjacent), fork(difference,
        identity, fork(sfilter, identity, chain(rbind(compose, first),
        lbind(rbind, equality), mostcolor))))), fork(difference, identity,
        fork(sfilter, identity, chain(rbind(compose, first), lbind(rbind,
        equality), mostcolor))))))), apply_func(lbind(compose, toindices),
        fork(shift, apply_func(lbind(compose, fork(sfilter, identity, chain
        (rbind(compose, first), lbind(rbind, equality), mostcolor))), fork(
        shift, vmirror, fork(multiply, shape, chain(tojvec, last, fork(
        position, fork(sfilter, identity, chain(rbind(compose, first),
        lbind(rbind, equality), mostcolor)), fork(difference, identity,
        fork(sfilter, identity, chain(rbind(compose, first), lbind(rbind,
        equality), mostcolor)))))))), apply_func(lbind(compose, compose(
        crement, invert)), chain(tojvec, last, fork(position, fork(sfilter,
        identity, chain(rbind(compose, first), lbind(rbind, equality),
        mostcolor)), fork(difference, identity, fork(sfilter, identity,
        chain(rbind(compose, first), lbind(rbind, equality), mostcolor)))))
        ))))), fork(shift, apply_func(lbind(compose, fork(sfilter, identity,
        chain(rbind(compose, first), lbind(rbind, equality), mostcolor))),
        fork(shift, vmirror, fork(multiply, shape, chain(tojvec, last, fork
        (position, fork(sfilter, identity, chain(rbind(compose, first),
        lbind(rbind, equality), mostcolor)), fork(difference, identity,
        fork(sfilter, identity, chain(rbind(compose, first), lbind(rbind,
        equality), mostcolor)))))))), apply_func(lbind(compose, compose(
        crement, invert)), chain(tojvec, last, fork(position, fork(sfilter,
        identity, chain(rbind(compose, first), lbind(rbind, equality),
        mostcolor)), fork(difference, identity, fork(sfilter, identity,
        chain(rbind(compose, first), lbind(rbind, equality), mostcolor)))))
        ))), objects(I, F, T, T))), mapply(fork(recolor, chain(lbind(index,
        I), first, fork(intersection, apply_func(lbind(compose, toindices),
        fork(combine, fork(insert, fork(extract, fork(sfilter, identity,
        chain(rbind(compose, first), lbind(rbind, equality), mostcolor)),
        chain(rbind(compose, initset), lbind(rbind, adjacent), fork(
        difference, identity, fork(sfilter, identity, chain(rbind(compose,
        first), lbind(rbind, equality), mostcolor))))), fork(difference,
        identity, fork(sfilter, identity, chain(rbind(compose, first),
        lbind(rbind, equality), mostcolor)))), chain(lbind(recolor, ZERO),
        delta, fork(insert, fork(extract, fork(sfilter, identity, chain(
        rbind(compose, first), lbind(rbind, equality), mostcolor)), chain(
        rbind(compose, initset), lbind(rbind, adjacent), fork(difference,
        identity, fork(sfilter, identity, chain(rbind(compose, first),
        lbind(rbind, equality), mostcolor))))), fork(difference, identity,
        fork(sfilter, identity, chain(rbind(compose, first), lbind(rbind,
        equality), mostcolor))))))), apply_func(lbind(compose, toindices),
        fork(shift, apply_func(lbind(compose, fork(sfilter, identity, chain
        (rbind(compose, first), lbind(rbind, equality), mostcolor))), fork(
        shift, compose(hmirror, vmirror), fork(multiply, shape, fork(
        position, fork(sfilter, identity, chain(rbind(compose, first),
        lbind(rbind, equality), mostcolor)), fork(difference, identity,
        fork(sfilter, identity, chain(rbind(compose, first), lbind(rbind,
        equality), mostcolor))))))), apply_func(lbind(compose, compose(
        crement, invert)), fork(position, fork(sfilter, identity, chain(
        rbind(compose, first), lbind(rbind, equality), mostcolor)), fork(
        difference, identity, fork(sfilter, identity, chain(rbind(compose,
        first), lbind(rbind, equality), mostcolor))))))))), fork(shift,
        apply_func(lbind(compose, fork(sfilter, identity, chain(rbind(
        compose, first), lbind(rbind, equality), mostcolor))), fork(shift,
        compose(hmirror, vmirror), fork(multiply, shape, fork(position,
        fork(sfilter, identity, chain(rbind(compose, first), lbind(rbind,
        equality), mostcolor)), fork(difference, identity, fork(sfilter,
        identity, chain(rbind(compose, first), lbind(rbind, equality),
        mostcolor))))))), apply_func(lbind(compose, compose(crement, invert
        )), fork(position, fork(sfilter, identity, chain(rbind(compose,
        first), lbind(rbind, equality), mostcolor)), fork(difference,
        identity, fork(sfilter, identity, chain(rbind(compose, first),
        lbind(rbind, equality), mostcolor))))))), objects(I, F, T, T)))


def solve_97a05b5b(I):
    return paint(paint(subgrid(argmax(objects(I, F, T, T), size), I),
        mapply(fork(mapply, compose(lbind(lbind, shift), normalize), fork(
        apply, chain(compose(lbind(rbind, subtract), ulcorner), fork(
        combine, compose(lbind(recolor, ZERO), rbind(sfilter, compose(flip,
        matcher(first, TWO)))), rbind(sfilter, matcher(first, TWO))),
        normalize), fork(sfilter, compose(rbind(sfilter, chain(compose(
        positive, size), lbind(sfilter, apply(toindices, objects(switch(
        subgrid(argmax(objects(I, F, T, T), size), I), TWO, ZERO), T, T, T)
        )), lbind(lbind, contained))), chain(lbind(occurrences, switch(
        subgrid(argmax(objects(I, F, T, T), size), I), TWO, ZERO)), fork(
        combine, compose(lbind(recolor, ZERO), rbind(sfilter, compose(flip,
        matcher(first, TWO)))), rbind(sfilter, matcher(first, TWO))),
        normalize)), chain(rbind(compose, compose(chain(size, first, lbind(
        sfilter, apply(toindices, objects(switch(subgrid(argmax(objects(I,
        F, T, T), size), I), TWO, ZERO), T, T, T)))), lbind(lbind,
        contained))), lbind(rbind, equality), rbind(colorcount, TWO))))),
        mapply(lbind(rapply, apply(fork(compose, first, last), product(
        combine(astuple(cmirror, dmirror), astuple(hmirror, vmirror)),
        combine(astuple(cmirror, dmirror), astuple(hmirror, vmirror))))),
        sfilter(objects(I, F, T, T), compose(rbind(greater, ONE), numcolors
        ))))), mapply(fork(mapply, compose(lbind(lbind, shift), normalize),
        fork(apply, chain(compose(lbind(rbind, subtract), ulcorner), fork(
        combine, compose(lbind(recolor, ZERO), rbind(sfilter, compose(flip,
        matcher(first, TWO)))), rbind(sfilter, matcher(first, TWO))),
        normalize), chain(lbind(occurrences, switch(subgrid(argmax(objects(
        I, F, T, T), size), I), TWO, ZERO)), fork(combine, compose(lbind(
        recolor, ZERO), rbind(sfilter, compose(flip, matcher(first, TWO)))),
        rbind(sfilter, matcher(first, TWO))), normalize))), mapply(lbind(
        rapply, apply(fork(compose, first, last), product(combine(astuple(
        cmirror, dmirror), astuple(hmirror, vmirror)), combine(astuple(
        cmirror, dmirror), astuple(hmirror, vmirror))))), sfilter(sfilter(
        objects(I, F, T, T), compose(rbind(greater, ONE), numcolors)),
        chain(flip, rbind(contained, apply_func(lbind(remove, TWO), palette
        (mapply(fork(mapply, compose(lbind(lbind, shift), normalize), fork(
        apply, chain(compose(lbind(rbind, subtract), ulcorner), fork(
        combine, compose(lbind(recolor, ZERO), rbind(sfilter, compose(flip,
        matcher(first, TWO)))), rbind(sfilter, matcher(first, TWO))),
        normalize), fork(sfilter, compose(rbind(sfilter, chain(compose(
        positive, size), lbind(sfilter, apply(toindices, objects(switch(
        subgrid(argmax(objects(I, F, T, T), size), I), TWO, ZERO), T, T, T)
        )), lbind(lbind, contained))), chain(lbind(occurrences, switch(
        subgrid(argmax(objects(I, F, T, T), size), I), TWO, ZERO)), fork(
        combine, compose(lbind(recolor, ZERO), rbind(sfilter, compose(flip,
        matcher(first, TWO)))), rbind(sfilter, matcher(first, TWO))),
        normalize)), chain(rbind(compose, compose(chain(size, first, lbind(
        sfilter, apply(toindices, objects(switch(subgrid(argmax(objects(I,
        F, T, T), size), I), TWO, ZERO), T, T, T)))), lbind(lbind,
        contained))), lbind(rbind, equality), rbind(colorcount, TWO))))),
        mapply(lbind(rapply, apply(fork(compose, first, last), product(
        combine(astuple(cmirror, dmirror), astuple(hmirror, vmirror)),
        combine(astuple(cmirror, dmirror), astuple(hmirror, vmirror))))),
        sfilter(objects(I, F, T, T), compose(rbind(greater, ONE), numcolors
        ))))))), chain(first, lbind(remove, TWO), palette))))))


def solve_3e980e27(I):
    return paint(I, combine(mapply(apply_func(chain(rbind(compose, center),
        lbind(lbind, shift), fork(shift, identity, apply_func(compose(lbind
        (compose, compose(invert, ulcorner)), lbind(rbind, sfilter)), lbind
        (contained, TWO)))), vmirror(argmax(sfilter(insert(insert(astuple(
        THREE, invert(astuple(TEN, TEN))), initset(astuple(TWO, invert(
        astuple(TEN, TEN))))), objects(I, F, T, T)), compose(lbind(
        contained, TWO), palette)), size))), remove(argmax(sfilter(insert(
        insert(astuple(THREE, invert(astuple(TEN, TEN))), initset(astuple(
        TWO, invert(astuple(TEN, TEN))))), objects(I, F, T, T)), compose(
        lbind(contained, TWO), palette)), size), sfilter(insert(insert(
        astuple(THREE, invert(astuple(TEN, TEN))), initset(astuple(TWO,
        invert(astuple(TEN, TEN))))), objects(I, F, T, T)), compose(lbind(
        contained, TWO), palette)))), mapply(apply_func(chain(rbind(compose,
        center), lbind(lbind, shift), fork(shift, identity, apply_func(
        compose(lbind(compose, compose(invert, ulcorner)), lbind(rbind,
        sfilter)), lbind(contained, THREE)))), argmax(sfilter(insert(insert
        (astuple(THREE, invert(astuple(TEN, TEN))), initset(astuple(TWO,
        invert(astuple(TEN, TEN))))), objects(I, F, T, T)), compose(lbind(
        contained, THREE), palette)), size)), remove(argmax(sfilter(insert(
        insert(astuple(THREE, invert(astuple(TEN, TEN))), initset(astuple(
        TWO, invert(astuple(TEN, TEN))))), objects(I, F, T, T)), compose(
        lbind(contained, THREE), palette)), size), sfilter(insert(insert(
        astuple(THREE, invert(astuple(TEN, TEN))), initset(astuple(TWO,
        invert(astuple(TEN, TEN))))), objects(I, F, T, T)), compose(lbind(
        contained, THREE), palette))))))
