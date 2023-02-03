'''
Defines a class, Neuron472912177, of neurons from Allen Brain Institute's model 472912177

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472912177:
    def __init__(self, name="Neuron472912177", x=0, y=0, z=0):
        '''Instantiate Neuron472912177.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472912177_instance is used instead
        '''
               
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Pvalb-IRES-Cre_Ai14_IVSCC_-176847.04.02.01_470522102_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
 
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472912177_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im_v2', u'K_T', u'Kd', u'Kv2like', u'Kv3_1', u'NaV', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 143.65
            sec.e_pas = -95.5370941162
        
        for sec in self.axon:
            sec.cm = 2.16
            sec.g_pas = 0.000662463571112
        for sec in self.dend:
            sec.cm = 2.16
            sec.g_pas = 9.80198332219e-06
        for sec in self.soma:
            sec.cm = 2.16
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Ih = 5.11629e-05
            sec.gbar_NaV = 0.0585202
            sec.gbar_Kd = 0.000311925
            sec.gbar_Kv2like = 0.0510602
            sec.gbar_Kv3_1 = 0.650761
            sec.gbar_K_T = 0.0333859
            sec.gbar_Im_v2 = 0.00775049
            sec.gbar_SK = 0.00273401
            sec.gbar_Ca_HVA = 0.00056479
            sec.gbar_Ca_LVA = 0.00321148
            sec.gamma_CaDynamics = 0.00772044
            sec.decay_CaDynamics = 20.3002
            sec.g_pas = 0.000267055
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

