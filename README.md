# ml_pipeline
simple ml pipeline with DVC(Data Version Control)
              +-----------+       
              | load_data |       
              +-----------+       
                    *             
                    *             
                    *             
             +------------+       
             | split_data |       
             +------------+       
             **           **      
           **               **    
         **                   **  
+------------+                  **
| train_data |                **  
+------------+              **    
             **           **      
               **       **        
                 **   **          
              +----------+        
              | evaluate | 
