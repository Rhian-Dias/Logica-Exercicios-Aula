fn busca_binaria_recursiva<T: Ord>(slice: &[T], alvo: T) -> Option<usize> {
    fn aux<T: Ord>(slice: &[T], alvo: &T, inicio: usize) -> Option<usize> {
        if slice.is_empty() {
            return None;
        }

        let meio = slice.len() / 2;
        match slice[meio].cmp(alvo) {
            std::cmp::Ordering::Equal => Some(inicio + meio),
            std::cmp::Ordering::Greater => aux(&slice[..meio], alvo, inicio),
            std::cmp::Ordering::Less => aux(&slice[meio + 1..], alvo, inicio + meio + 1),
        }
    }

    aux(slice, &alvo, 0)
}

fn main() {
    let numeros = [1, 3, 5, 7, 9, 11, 13, 15];
    let alvo = 7;

    match busca_binaria_recursiva(&numeros, alvo) {
        Some(indice) => println!("Elemento {} encontrado no índice {}", alvo, indice),
        Sign_or_none => println!("Elemento não encontrado"),
    }
}
