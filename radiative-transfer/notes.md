## Definitions

t_c is the continuum optical depth, it's a constant background opacity added at every frequency.

t_l is the line optical depth scale. it controls the strenght of the spectral line opacity, distributed over frequency using the lorentz line profile.

## Answers to questions.

1. Setting I0 and t_c to zero.

    - Setting t_c to means that the optical depth becomes almost zero and the outgoing intensiti stays close to the incoming intensity I0.

    Near the lince center t_l still gives opacity, so, the intensity can change very strongly here.

    [initial setting]

    - Increasing t_l makes so the intensity near the line center pushes more strongly towards the source function S, while decreasing it makes so the spectrum stays closer to the incoming intensity I0.

    [increasing tau]

    - The line saturates if we increase t_l a lot

    [saturated line]

    - Since the radiative transfer's equation is:
    I=I_0 e^-τ + S(1−e^−τ)

    and for t_c = 0 we have that t_v = t_c + phi(v) * t_l, at line center phi(0) = 0.64

    hence t_0 = 0.64

    and for saturation to occurr we need t >> 1 and this is not the case

    [tau equals 1]

2. If we set t_l between 0 and 1 and increase I0 the emission line starts to squeeze, till the point that I0 is greater than the source function, at that point we have an absorption line!

    [the first absorption line]

3. If we really saturate both the emission and the absorption lines we can see that there is foundamentally no difference, as the Intensity becomes equal to the Source function. The saturation is the same in both cases but where it looks like absorption or emission depends on whether that source function is below or above the background intensity

    [extremly saturated emission]

    [extremly saturated absorption]


4. When both t_l and t_c are zero it means that the that the transfer equation becomes I_v(D) = I_v(0)
and that the slab is completely transparent

we can see from the plot that there is no spectral line.

    [both taus are zero]

5. for t_c different from zero, increasing the value pushes the tails of the line spectra closer to the source function both for I_0 < S and I_0 > S

    For t_c != 0 the wings are not transparent anymore, since far from the line center t_v ≈ t_c.

    Example with t_l = 5 and t_c = 1. At line center phi(0) ≈ 0.64, so:

    t_center = t_c + t_l phi(0) = 1 + 5 * 0.64 = 4.2

    If I_0 = 10 and S = 50:

    I_wing = 50 + (10 - 50)e^-1 ≈ 35.3
    I_center = 50 + (10 - 50)e^-4.2 ≈ 49.4

    so the line is in emission and tends toward S.

    If I_0 = 80 and S = 30:

    I_wing = 30 + (80 - 30)e^-1 ≈ 48.4
    I_center = 30 + (80 - 30)e^-4.2 ≈ 30.8

    so the line is in absorption and also tends toward S.

    [figure_10_50_1]

    [figure_80_30_1]

6. An unsaturated line has approximately the same shape as the line opacity profile. In this case that profile is Lorentzian, so the line appears as a smooth peak in emission or a smooth dip in absorption, with wings on both sides.

    This happens because the optical depth is still small, so the radiation is only weakly changed by the slab. The line intensity therefore follows where the opacity is largest: the strongest change is at line center, while the effect becomes weaker in the wings.


7. t_c = t_l does not have a special physical meaning by itself. It only means that the chosen continuum optical depth and line optical depth scale have the same value. The actual line effect still changes with frequency because it is multiplied by the line profile.


8. [optically thick emission line]

    In the optically thick emission case the line center has a very large optical depth, so the emerging intensity becomes almost equal to the source function S. The wings are less optically thick, so they stay closer to the incoming intensity I_0, giving a strong emission feature.

9. Reducing the damping makes the line much thinner because the opacity is concentrated closer to the line center. The wings become weaker, so the line affects only a narrow range of frequencies, while the center can still change strongly.

[t_c 0 and t_1 normal damping]

[t_c 0 and t_1 small damping]

    

