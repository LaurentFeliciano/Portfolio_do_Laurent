/* *******************************************************************
* Colegio Técnico Antônio Teixeira Fernandes (Univap)
* Curso Técnico em Informática - Data de Entrega: 14/08/2020
* Autores do Projeto: Laurent Chaves Assis Feliciano
* Turma: 2F-Informática
* Atividade 5
* Observação: nenhuma
* Exercício3.cs
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
            int AnoInicial = int.Parse(textBox1.Text);
            int AnoFinal = int.Parse(textBox2.Text);
            textBox1.Clear();
            textBox2.Clear();
            int C=0;
            for (C = AnoInicial; C <= AnoFinal; C++)
            {
                if (DateTime.IsLeapYear(C))
                    textBox3.AppendText(C + " é Ano Bissexto" + Environment.NewLine);
                else
                    textBox3.AppendText(C + " não é Ano Bissexto" + Environment.NewLine);
            }
        }
    }
}