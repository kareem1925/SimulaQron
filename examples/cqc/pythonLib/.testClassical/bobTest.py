#
# Copyright (c) 2017, Stephanie Wehner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. All advertising materials mentioning features or use of this software
#    must display the following acknowledgement:
#    This product includes software developed by Stephanie Wehner, QuTech.
# 4. Neither the name of the QuTech organization nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import socket

from SimulaQron.general.hostConfig import *
from SimulaQron.cqc.backend.cqcHeader import *
from SimulaQron.cqc.pythonLib.cqc import *


def recv_classical():
	buf=bytearray()
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(('',8831))
	s.listen(1)
	(conn,addr)=s.accept()
	while True:
		data=conn.recv(1024)
		if not data:
			break
		buf+=data
	conn.close()
	return list(buf)


#####################################################################################################
#
# main
#
def main():

	# Initialize the connection
	Bob=CQCConnection("Bob")

	# Make an EPR pair with Alice
	qB=Bob.createEPR("Alice")

	# Receive info about corrections
	data=recv_classical())

	# Apply corrections
	if b==1:
		qB.X()
	if a==1:
		qB.Z()

	# Measure qubit
	m=qB.measure()
	print("App {}: Measurement outcome is: {}".format(Bob.name,m))

	# Stop the connection
	Bob.close()


##################################################################################################
main()
