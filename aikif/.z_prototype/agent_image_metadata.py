# agent_image_metadata.py		written by Duncan Murray	16/4/2015


import os
import aikif.config as cfg
import aikif.agents.agent as agt
import aikif.toolbox.image_tools as mod_img

class ImageMetadataAgent(agt.Agent):
    """
    takes a list of image files (collected via agent.gather.agent_filelist)
    and extracts picture metadata to a CSV file
    """

    def __init__(self, name, ip_file, op_file):
        """
        running and fldr are not needed for this agent
        so using defaults
        """
        agt.Agent.__init__(self, name,  fldr=os.getcwd(), running=True)
        self.ip_file = ip_file
        self.op_file = op_file
        self.do_your_job()

    def do_your_job(self):
        """
        collect metadata on images
        """ 
        with open(self.ip_file, 'r') as ip:
            with open(self.op_file, 'w') as op:
                for c in mod_img.metadata_header():
                    op.write('"' + c + '",')
                op.write('\n')
                for line in ip:
                    #fname = line.replace('\\', '\\\\').strip()
                    fname = line.strip().strip(',').strip('"')
                    #print('fname = ', fname)
                    if os.path.isfile(os.path.abspath(fname)):
                        dat = mod_img.get_metadata_as_csv(fname)
                        #print(dat)
                        op.write(dat + '\n')
                    else:
                        print(('cant get metadata for file ' + fname))
    
