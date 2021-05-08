# Reproducing Low-Rate TCP-Targeted Denial of Service Attacks

 In this report, we reproduce the main findings of Low-Rate TCP-Targeted Denial of Service Attacks. This paper introduces the low-rate "shrew" Denial of Service attacks. Compared to high-rate TCP-targeted DoS attacks, shrew attacks are more dangerous, and more unlikely to be detected by TCP due to their low average rate attack. Whenever TCP recognises congestion in the network, it doubles the retransmission timeout(RTO) starting at an RTO value of 1second, resends the packet and waits for the timeout. During this time period, attacker can throttle the network with large enough TCP flow causing the retransmitted packet to drop. Sender doubles the RTO again and tries to retransmit. 

 The shrew attacks are of two-level periodic square wave stream in which the attacker transmits bursts of duration l and rate R in a deterministic on-off pattern that has period T. In the paper, the outages are created at times 3,7,15,... to successfully launch the attack while avoiding being detected.
 
<p float="left">
<img src="sqaure_wave.png" alt="drawing" width="400"/>
</p>
 
 
We use Mininet on Amazon EC2 to create a simulated network, designing network layout, and choosing our own network bandwidth and delay, re-create the results in this paper. We test the low-rate DoS attacks in four scenarios depicted in the graph below.

![multi](https://user-images.githubusercontent.com/32016647/117553305-cd038700-b01e-11eb-8124-c52f3afa502e.png)
