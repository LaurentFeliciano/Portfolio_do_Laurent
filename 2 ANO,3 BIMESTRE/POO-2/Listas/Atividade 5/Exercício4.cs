/* *******************************************************************
* Colegio Técnico Antônio Teixeira Fernandes (Univap)
* Curso Técnico em Informática - Data de Entrega: 14/08/2020
* Autores do Projeto: Laurent Chaves Assis Feliciano
* Turma: 2F-Informática
* Atividade 5
* Observação: nenhuma
* Exercício4.cs
* ************************************************************/
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Forms
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int Dia= int.Parse(textBox1.Text);
            int Mes = int.Parse(textBox2.Text);
            int Ano = int.Parse(textBox3.Text);
            int V = int.Parse(textBox4.Text);
            textBox4.Clear();
            DateTime Data = new DateTime(Ano, Mes, Dia);
            if ((V % 3 == 0) && ((V / 3) % 2 == 1 ))
            {
                DateTime DataFinal = Data.AddDays(V / 3 - 2);
                label4.Text = DataFinal.ToString("dd/MM/yy") + "";
            }
            else
            {
                MessageBox.Show("Valor da Soma Inválido, Tente Novamente com outros Valores");
                return;
            }
        }
    }
}
