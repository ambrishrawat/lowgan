import tensorflow as tf


class gan():
    '''
    a simple 1-D density estimator using GAN architechture
    '''

    def __init__(self):
        pass

    def _create_ops(self):
        ''' 
        create ops 
        '''

        with tf.variable_scope('D_'):
            '''
            discrinimiator ops
            '''
            #input and output placegolders (setimating 1-D distribution here)
            self.D_inp = tf.placeholder(tf.float32, shape = (self.batch_size,1))
            self.D_tar =  tf.placeholder(tf.float32, shape = (self.batch_size,1))

            D_pred = discriminator(self.D_inp,self.batch_size)

            self.D_loss = tf.reduce_mean(tf.square(D_pred - self.D_tar))
            self.D_opt = 


        with tf.variable_scope('G_'):
            '''
            generator ops
            '''

            self.G_z = tf.placefolder(tf.float32, shape = (self.batch_size,1))
            self.G_pred = generator()
        

    def train(self):
        pass
