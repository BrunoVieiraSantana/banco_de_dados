"Error_duplicate"
"Error_email_invalid"
"Error_date"

        except(psycopg2.errors.UniqueViolation):
            return "Error"


            self.fifth_frame_entry_update_motorista.delete(0, END)
            self.fifth_frame_entry_name_update_motorista.delete(0, END)
            self.fifth_frame_entry_cpf_update_motorista.delete(0, END)
            self.fifth_frame_entry_cnh_update_motorista.delete(0, END)
            for item in self.fifth_frame_table_search_update_motorista.get_children():
                self.fifth_frame_table_search_update_motorista.delete(item)