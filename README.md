# &#181;Phone
A baby phone running on MicroPython. This is currently work in
progress.

[![Build Status](https://travis-ci.org/windisch/uPhone.svg?branch=master)](https://travis-ci.org/windisch/uPhone)


## Why?
All baby phones suck, but some are useful! Most baby phones available
come with a lot of unnecessary features, unwiedly client devices,
heavy power consumption, and insufficient range. This is challenging
in most outdoor scenarios, when your kid is just around the corner,
but not within earshot. The functionality of the &#181;Phone is as
slim as possible to provide reliable baby monitoring in situations
when there is no outlet in sight. I try to make the client as slim as
possible as well to allow any possible end devices (technically
speaking, any device which is able to open network sockets).


## Components
I currently used a [Pybord D-series with
WiFi](https://store.micropython.org/product/PYBD-SF2-W4F2) and
attached cheap noise sensor to it (Max4466).
