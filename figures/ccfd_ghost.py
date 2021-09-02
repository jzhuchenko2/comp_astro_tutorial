import numpy as np
import matplotlib.pyplot as plt
import grid_plot as gp

# plot a simple finite-difference grid

#-----------------------------------------------------------------------------

nzones = 7
ng = 1

# data that lives on the grid
#a = np.array([0.3, 1.0, 0.9, 0.8, 0.25, 0.15, 0.5, 0.55])
#a = np.array([0.3, 1.0, 0.9, 0.8, 0.25, 0.1, 0.5, 0.55])
a = np.array([1.0, 0.9, 0.8, 0.25, 0.1, 0.5, 0.55])

gr = gp.FVGrid(nzones, ng)

aa = gr.scratch_array()
aa[gr.ilo:gr.ihi+1] = a

cc = gp.CellCentered(gr, aa)

plt.clf()

gr.draw_grid(draw_ghost=1, emphasize_end=1)

gr.label_center(ng+nzones//2,   r"$i$")
gr.label_center(ng+nzones//2-1, r"$i-1$")
gr.label_center(ng+nzones//2+1, r"$i+1$")

gr.label_center(gr.ilo, r"$\mathrm{lo}$")
gr.label_center(gr.ilo-1, r"$\mathrm{lo-1}$")

gr.label_center(gr.ihi, r"$\mathrm{hi}$")
gr.label_center(gr.ihi+1, r"$\mathrm{hi+1}$")

# draw the data
for i in range(nzones):
    cc.draw_data_point(ng+i, color="r")    
    
cc.label_data_point(ng+nzones//2, r"$\phi_i$", color="r")

# label dx
gr.label_dx(gr.ng+nzones//2)

gr.clean_axes(show_ghost=True, pad_fac=0.02, ylim=(-0.5, 1.6))

f = plt.gcf()
f.set_size_inches(10.0,2.5)

plt.savefig("ccfd_ghost.png", dpi=100)
