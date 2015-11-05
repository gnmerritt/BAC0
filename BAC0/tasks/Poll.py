#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 by Christian Tremblay, P.Eng <christian.tremblay@servisys.com>
#
# Licensed under LGPLv3, see file LICENSE in this source tree.
"""
Repeat read function every delay
"""

from .TaskManager import Task

class Poll(Task):
    """
    Will fit fan status with fan command
    """

    def __init__(self, point, *, delay=10):
        """
        :param point: (BAC0.core.device.Points.Point) name of the point to read
        :param delay: (int) Delay between reads in seconds, defaults = 10sec
        
        A delay cannot be < 0.5sec (there are risks of overloading the device)

        :returns: Nothing
        """
        if delay < 0.5:
            delay = 0.5
        if point.properties:
            self._point = point
            Task.__init__(self, delay=delay)
        else:
            raise ValueError('Should provide a point object')

    def task(self):
        self._point.value
