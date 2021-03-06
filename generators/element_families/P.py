# -*- coding: utf-8 -*-

P = {
    "P1_interval": {
        "id": "P_P1_interval",
        "label": "\mathsf{P}_{\mathsf{1}}",
        "dimension": 2,
        "image": "P1_interval.png",
        "weight_functions": "\dofm{2}{1}{0}{0}{1} = 2",
        "exterior_calc": "\P{1}{0}{1}",
        "code": '("P", interval, 1)',
        "code_alt": '("P", interval, 1, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P2_interval": {
        "id": "P_P2_interval",
        "label": "\mathsf{P}_{\mathsf{2}}",
        "dimension": 3,
        "image": "P2_interval.png",
        "weight_functions": "\dofm{2}{2}{0}{0}{1} \pl \dofm{1}{1}{1}{1}{1} = 3",
        "exterior_calc": "\P{2}{0}{1}",
        "code": '("P", interval, 2)',
        "code_alt": '("P", interval, 2, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P3_interval": {
        "id": "P_P3_interval",
        "label": "\mathsf{P}_{\mathsf{3}}",
        "dimension": 4,
        "image": "P3_interval.png",
        "weight_functions": "\dofm{2}{3}{0}{0}{1} \pl \dofm{1}{2}{1}{1}{2} = 4",
        "exterior_calc": "\P{3}{0}{1}",
        "code": '("P", interval, 3)',
        "code_alt": '("P", interval, 3, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "dP1_interval": {
        "id": "P_dP1_interval",
        "label": "\mathsf{dP}_{\mathsf{1}}",
        "dimension": 2,
        "image": "dP1_interval.png",
        "weight_functions": "\dofm{1}{1}{0}{1}{2} = 2",
        "exterior_calc": "\P{1}{1}{1}",
        "code": '("DP", interval, 1)',
        "code_alt": '("P", interval, 1, 1)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP2_interval": {
        "id": "P_dP2_interval",
        "label": "\mathsf{dP}_{\mathsf{2}}",
        "dimension": 3,
        "image": "dP2_interval.png",
        "weight_functions": "\dofm{1}{2}{0}{1}{3} = 3",
        "exterior_calc": "\P{2}{1}{1}",
        "code": '("DP", interval, 2)',
        "code_alt": '("P", interval, 2, 1)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP3_interval": {
        "id": "P_dP3_interval",
        "label": "\mathsf{dP}_{\mathsf{3}}",
        "dimension": 4,
        "image": "dP3_interval.png",
        "weight_functions": "\dofm{1}{3}{0}{1}{4} = 4",
        "exterior_calc": "\P{3}{1}{1}",
        "code": '("DP", interval, 3)',
        "code_alt": '("P", interval, 3, 1)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "P1_triangle": {
        "id": "P_P1_triangle",
        "label": "\mathsf{P}_{\mathsf{1}}",
        "dimension": 3,
        "image": "P1_triangle.png",
        "weight_functions": "\dofm{3}{1}{0}{0}{1} = 3",
        "exterior_calc": "\P{1}{0}{2}",
        "code": '("P", triangle, 1)',
        "code_alt": '("P", triangle, 1, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P2_triangle": {
        "id": "P_P2_triangle",
        "label": "\mathsf{P}_{\mathsf{2}}",
        "dimension": 6,
        "image": "P2_triangle.png",
        "weight_functions": "\dofm{3}{2}{0}{0}{1} \pl \dofm{3}{1}{1}{1}{1} = 6",
        "exterior_calc": "\P{2}{0}{2}",
        "code": '("P", triangle, 2)',
        "code_alt": '("P", triangle, 2, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P3_triangle": {
        "id": "P_P3_triangle",
        "label": "\mathsf{P}_{\mathsf{3}}",
        "dimension": 10,
        "image": "P3_triangle.png",
        "weight_functions": "\dofm{3}{3}{0}{0}{1} \pl \dofm{3}{2}{1}{1}{2} \pl \dofm{1}{1}{2}{2}{1} = 10",
        "exterior_calc": "\P{3}{0}{2}",
        "code": '("P", triangle, 3)',
        "code_alt": '("P", triangle, 3, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "BDM1_triangle": {
        "id": "P_BDM1_triangle",
        "label": "\mathsf{BDM}^{\mathsf{[e/f]}}_{\mathsf{1}}",
        "dimension": 6,
        "image": "BDM1_triangle.png",
        "weight_functions": "\dofm{3}{1}{0}{1}{2} = 6",
        "exterior_calc": "\P{1}{1}{2}",
        "code": '("BDM[E,F]", triangle, 1)',
        "code_alt": '("P", triangle, 1, 1)',
        "color": "orange",
        "citation": "Brezzi, Douglas, and Marini, Numer. Math. 47 (1985)"
    },
    "BDM2_triangle": {
        "id": "P_BDM2_triangle",
        "label": "\mathsf{BDM}^{\mathsf{[e/f]}}_{\mathsf{2}}",
        "dimension": 12,
        "image": "BDM2_triangle.png",
        "weight_functions": "\dofm{3}{2}{0}{1}{3} \pl \dofm{1}{1}{1}{2}{3} = 12",
        "exterior_calc": "\P{2}{1}{2}",
        "code": '("BDM[E,F]", triangle, 2)',
        "code_alt": '("P", triangle, 2, 1)',
        "color": "orange",
        "citation": "Brezzi, Douglas, and Marini, Numer. Math. 47 (1985)"
    },
    "BDM3_triangle": {
        "id": "P_BDM3_triangle",
        "label": "\mathsf{BDM}^{\mathsf{[e/f]}}_{\mathsf{3}}",
        "dimension": 20,
        "image": "BDM3_triangle.png",
        "weight_functions": "\dofm{3}{3}{0}{1}{4} \pl \dofm{1}{2}{1}{2}{8} = 20",
        "exterior_calc": "\P{3}{1}{2}",
        "code": '("BDM[E,F]", triangle, 3)',
        "code_alt": '("P", triangle, 3, 1)',
        "color": "orange",
        "citation": "Brezzi, Douglas, and Marini, Numer. Math. 47 (1985)"
    },
    "dP1_triangle": {
        "id": "P_dP1_triangle",
        "label": "\mathsf{dP}_{\mathsf{1}}",
        "dimension": 3,
        "image": "dP1_triangle.png",
        "weight_functions": "\dofm{1}{1}{0}{2}{3} = 3",
        "exterior_calc": "\P{1}{2}{2}",
        "code": '("DP", triangle, 1)',
        "code_alt": '("P", triangle, 1, 2)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP2_triangle": {
        "id": "P_dP2_triangle",
        "label": "\mathsf{dP}_{\mathsf{2}}",
        "dimension": 6,
        "image": "dP2_triangle.png",
        "weight_functions": "\dofm{1}{2}{0}{2}{6} = 6",
        "exterior_calc": "\P{2}{2}{2}",
        "code": '("DP", triangle, 2)',
        "code_alt": '("P", triangle, 2, 2)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP3_triangle": {
        "id": "P_dP3_triangle",
        "label": "\mathsf{dP}_{\mathsf{3}}",
        "dimension": 10,
        "image": "dP3_triangle.png",
        "weight_functions": "\dofm{1}{3}{0}{2}{10} = 10",
        "exterior_calc": "\P{3}{2}{2}",
        "code": '("DP", triangle, 3)',
        "code_alt": '("P", triangle, 3, 2)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "P1_tetrahedron": {
        "id": "P_P1_tetrahedron",
        "label": "\mathsf{P}_{\mathsf{1}}",
        "dimension": 4,
        "image": "P1_tetrahedron.png",
        "weight_functions": "\dofm{4}{1}{0}{0}{1} = 4",
        "exterior_calc": "\P{1}{0}{3}",
        "code": '("P", tetrahedron, 1)',
        "code_alt": '("P", tetrahedron, 1, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P2_tetrahedron": {
        "id": "P_P2_tetrahedron",
        "label": "\mathsf{P}_{\mathsf{2}}",
        "dimension": 10,
        "image": "P2_tetrahedron.png",
        "weight_functions": "\dofm{4}{2}{0}{0}{1} \pl \dofm{6}{1}{1}{1}{1} = 10",
        "exterior_calc": "\P{2}{0}{3}",
        "code": '("P", tetrahedron, 2)',
        "code_alt": '("P", tetrahedron, 2, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P3_tetrahedron": {
        "id": "P_P3_tetrahedron",
        "label": "\mathsf{P}_{\mathsf{3}}",
        "dimension": 20,
        "image": "P3_tetrahedron.png",
        "weight_functions": "\dofm{4}{3}{0}{0}{1} \pl \dofm{6}{2}{1}{1}{2} \pl \dofm{4}{1}{2}{2}{1} = 20",
        "exterior_calc": "\P{3}{0}{3}",
        "code": '("P", tetrahedron, 3)',
        "code_alt": '("P", tetrahedron, 3, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "N2e1_tetrahedron": {
        "id": "P_N2e1_tetrahedron",
        "label": "\mathsf{N2}^{\mathsf{e}}_{\mathsf{1}}",
        "dimension": 12,
        "image": "N2e1_tetrahedron.png",
        "weight_functions": "\dofm{6}{1}{0}{1}{2} = 12",
        "exterior_calc": "\P{1}{1}{3}",
        "code": '("N2E", tetrahedron, 1)',
        "code_alt": '("P", tetrahedron, 1, 1)',
        "color": "red",
        "citation": u"Nédélec, Numer. Math. 50 (1986)"
    },
    "N2e2_tetrahedron": {
        "id": "P_N2e2_tetrahedron",
        "label": "\mathsf{N2}^{\mathsf{e}}_{\mathsf{2}}",
        "dimension": 30,
        "image": "N2e2_tetrahedron.png",
        "weight_functions": "\dofm{6}{2}{0}{1}{3} \pl \dofm{4}{1}{1}{2}{3} = 30",
        "exterior_calc": "\P{2}{1}{3}",
        "code": '("N2E", tetrahedron, 2)',
        "code_alt": '("P", tetrahedron, 2, 1)',
        "color": "red",
        "citation": u"Nédélec, Numer. Math. 50 (1986)"
    },
    "N2e3_tetrahedron": {
        "id": "P_N2e3_tetrahedron",
        "label": "\mathsf{N2}^{\mathsf{e}}_{\mathsf{3}}",
        "dimension": 60,
        "image": "N2e3_tetrahedron.png",
        "weight_functions": "\dofm{6}{3}{0}{1}{4} \pl \dofm{4}{2}{1}{2}{8} \pl \dofm{1}{1}{2}{3}{4} = 60",
        "exterior_calc": "\P{3}{1}{3}",
        "code": '("N2E", tetrahedron, 3)',
        "code_alt": '("P", tetrahedron, 3, 1)',
        "color": "red",
        "citation": u"Nédélec, Numer. Math. 50 (1986)"
    },
    "N2f1_tetrahedron": {
        "id": "P_N2f1_tetrahedron",
        "label": "\mathsf{N2}^{\mathsf{f}}_{\mathsf{1}}",
        "dimension": 12,
        "image": "N2f1_tetrahedron.png",
        "weight_functions": "\dofm{4}{1}{0}{2}{3} = 12",
        "exterior_calc": "\P{1}{2}{3}",
        "code": '("N2F", tetrahedron, 1)',
        "code_alt": '("P", tetrahedron, 1, 2)',
        "color": "yellow",
        "citation": u"Nédélec, Numer. Math. 50 (1986)"
    },
    "N2f2_tetrahedron": {
        "id": "P_N2f2_tetrahedron",
        "label": "\mathsf{N2}^{\mathsf{f}}_{\mathsf{2}}",
        "dimension": 30,
        "image": "N2f2_tetrahedron.png",
        "weight_functions": "\dofm{4}{2}{0}{2}{6} \pl \dofm{1}{1}{1}{3}{6} = 30",
        "exterior_calc": "\P{2}{2}{3}",
        "code": '("N2F", tetrahedron, 2)',
        "code_alt": '("P", tetrahedron, 2, 2)',
        "color": "yellow",
        "citation": u"Nédélec, Numer. Math. 50 (1986)"
    },
    "N2f3_tetrahedron": {
        "id": "P_N2f3_tetrahedron",
        "label": "\mathsf{N2}^{\mathsf{f}}_{\mathsf{3}}",
        "dimension": 60,
        "image": "N2f3_tetrahedron.png",
        "weight_functions": "\dofm{4}{3}{0}{2}{10} \pl \dofm{1}{2}{1}{3}{20} = 60",
        "exterior_calc": "\P{3}{2}{3}",
        "code": '("N2F", tetrahedron, 3)',
        "code_alt": '("P", tetrahedron, 3, 2)',
        "color": "yellow",
        "citation": u"Nédélec, Numer. Math. 50 (1986)"
    },
    "dP1_tetrahedron": {
        "id": "P_dP1_tetrahedron",
        "label": "\mathsf{dP}_{\mathsf{1}}",
        "dimension": 4,
        "image": "dP1_tetrahedron.png",
        "weight_functions": "\dofm{1}{1}{0}{3}{4} = 4",
        "exterior_calc": "\P{1}{3}{3}",
        "code": '("DP", tetrahedron, 1)',
        "code_alt": '("P", tetrahedron, 1, 3)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP2_tetrahedron": {
        "id": "P_dP2_tetrahedron",
        "label": "\mathsf{dP}_{\mathsf{2}}",
        "dimension": 10,
        "image": "dP2_tetrahedron.png",
        "weight_functions": "\dofm{1}{2}{0}{3}{10} = 10",
        "exterior_calc": "\P{2}{3}{3}",
        "code": '("DP", tetrahedron, 2)',
        "code_alt": '("P", tetrahedron, 2, 3)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP3_tetrahedron": {
        "id": "P_dP3_tetrahedron",
        "label": "\mathsf{dP}_{\mathsf{3}}",
        "dimension": 20,
        "image": "dP3_tetrahedron.png",
        "weight_functions": "\dofm{1}{3}{0}{3}{20} = 20",
        "exterior_calc": "\P{3}{3}{3}",
        "code": '("DP", tetrahedron, 3)',
        "code_alt": '("P", tetrahedron, 3, 3)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    }
}
